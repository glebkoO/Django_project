from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
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

def user_login(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Вы успешно прошли авторизацию')
				else:
					return HttpResponse('Аккаунт не существует')
			else:
				return HttpResponse('Ошибка')
	else:
		form = UserRegisterForm()
	return render(request, 'registration/login.html', {'form': form})


# class UserListView(ListView):
# 	template_name = 'registration/login.html'
# 	login_url = 'login'
# 	redirect_field_name = 'user_list'
#
# 	def get_queryset(self):
# 		return User.objects.filter(
# 			username=self.request.user
# 		)
def logout_user(request):
	return render(request, 'registration/logout.html', {})