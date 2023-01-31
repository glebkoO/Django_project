from django.http import request
from django.shortcuts import render, redirect
from . import models
# Create your views here.
def index(request):
    return render(request, 'Date/index.html')

