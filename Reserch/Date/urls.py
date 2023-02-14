from django import views
from django.urls import path
from . views import *
urlpatterns = [
    path('', index, name='home'),
    path('search/', SearchResult, name='search_results'),
    path('cabinet/', new_Date, name='cabinet'),
    path('success', success, name='success'),
]