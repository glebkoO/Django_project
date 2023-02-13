from django.urls import path, include
from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
    
]
