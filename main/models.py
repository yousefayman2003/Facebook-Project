from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import FileExtensionValidator

# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, date_of_birth, gender, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have an first name')
        if not last_name:
            raise ValueError('Users must have an last name')
        if not date_of_birth:
            raise ValueError('Users must have an date of birth')
        if not gender:
            raise ValueError('Users must have an gender')
        if not phone:
            raise ValueError('Users must have a phone number')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, date_of_birth, gender, phone, password):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            phone=phone
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    first_name = models.CharField(
        max_length=20, verbose_name='first name', default=None)
    last_name = models.CharField(
        max_length=20, verbose_name='last name', default=None)
    date_of_birth = models.DateField(
        verbose_name='date of birth', default=None)
    gender = models.CharField(
        max_length=6, verbose_name='gender', default=None, db_column='gender')
    phone = models.CharField(max_length=11, unique=True,
                             db_column='phone_number', verbose_name='phone number')
    about = models.TextField(max_length=1000)
    image = models.ImageField(default='default.png', upload_to='profile', validators=[
                              FileExtensionValidator(['png', 'jpg'])])
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    # some required fields for django
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'date_of_birth', 'gender', 'phone']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = 'user'


class PageModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='created_by', db_column='created_by')
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name='date_created')
    company_email = models.CharField(max_length=255)
    likes_number = models.IntegerField(
        verbose_name='likes_number', db_column='likes_number', default=0)

    class Meta:
        db_table = 'page'


class PostModel(models.Model):
    title = models.CharField(
        max_length=100, verbose_name='title', default=None)
    content = models.TextField(
        max_length=10000, verbose_name='content', default=None)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='created_by', db_column='created_by')
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name='date_created')
    likes_number = models.IntegerField(
        verbose_name='likes_number', db_column='likes_number', default=0)

    def __str__(self):
        return self.title

    def comment_count(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()

    class Meta:
        db_table = 'post'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content