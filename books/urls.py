from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('upload/', views.upload_book, name='upload_book'),
    path('signup/', views.signup, name='signup'),
    # path('profile/', views.profile, name='profile'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='books/logout_confirm.html'), name='logout'),

    # Password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='books/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='books/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='books/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='books/password_reset_complete.html'), name='password_reset_complete'),
]
