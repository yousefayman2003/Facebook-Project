from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('home/', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', auth_view.LoginView.as_view(
        template_name='registration/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('post_detail/<int:pk>', views.post_detail, name='post_detail'),
    path('post_edit/<int:pk>', views.post_edit, name='post_edit'),
    path('post_delete/<int:pk>', views.post_delete, name='post_delete'),


]
