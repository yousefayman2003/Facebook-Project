from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, PostModel, Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='', required=True,  widget=forms.TextInput(
        attrs={'placeholder': 'Email Address', 'rows': 1}), help_text='Required.')
    phone = forms.CharField(label='', max_length=11, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'rows': 1}))
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required.', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'rows': 1}))
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Required.', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'rows': 1}))
    date_of_birth = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2023)))
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect())

    password1 = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Password', 'rows': 1}))
    password2 = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Confirm Password', 'rows': 1}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone',
                  'password1', 'password2', 'date_of_birth', 'gender']

    # For removing help text
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(RegisterForm, self).__init__(*args, **kwargs)

        for name in ['first_name', 'last_name', 'email', 'phone',
                     'password1', 'password2', 'date_of_birth', 'gender']:
            self.fields[name].help_text = None


class PostingModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = PostModel
        fields = ['title', 'content']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        image = forms.ImageField()
        fields = ['email', 'phone', 'image']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['email', 'phone', 'image']:
            self.fields[fieldname].help_text = None


class PostingUpdateForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here.....'}))

    class Meta:
        model = Comment
        fields = ['content',]


class like_clicked(forms.ModelForm):
    button = forms.CharField(widget=forms.HiddenInput(), initial='Submit')

    class Meta:
        model = PostModel
        fields = ['button',]
