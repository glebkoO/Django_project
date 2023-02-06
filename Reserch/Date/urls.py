from django.urls import path
from . import views
from . views import *
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('register/', RegisterUser.as_view, name='register'),
]