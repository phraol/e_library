from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),        # Landing page
    path('home/', views.home, name='home'),         # Library page
    path('upload/', views.upload_book, name='upload_book'),

    # Login / logout
    path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
