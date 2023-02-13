from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'registration/register.html', {'form': form})
	
@login_required
def profile(request):
	return render(request, 'registration/profile.html')

def login_user(request):
	return render(request, 'registration/login.html', {})

def logout_user(request):
	pass