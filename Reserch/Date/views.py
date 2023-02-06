from django.contrib.auth.forms import UserCreationForm
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


from . import models
# Create your views here.
def index(request):
    return render(request, 'Date/index.html')

class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'Date/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
