from django.contrib import admin
from main.models import User, PostModel, Comment

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content',
                    'created_by', 'date_created', 'likes_number']


admin.site.register(User, UserAdmin)
admin.site.register(PostModel, PostAdmin)
admin.site.register(Comment)
