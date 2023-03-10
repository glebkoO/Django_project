from django.contrib.auth.forms import UserCreationForm
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q
from .models import *
from .forms import DateForm
from django.http import HttpResponse

from . models import *
# Create your views here.
def index(request):
    dates = Date.objects.all()
    context = {'dates': dates}
    return render(request, 'Date/index.html', context)

def SearchResult(request):
    if request.method == "GET":
        query = request.GET.get('case')
        if query == '':
            query = 'ничего не ввели'
        object_list = Date.objects.filter(Q(name__contains=query) | Q(pk__contains=query))
        
        context = {'query': query, 'object_list': object_list}
    return render(request, 'Date/search_results.html', context)
def new_Date(request):
    if request.method == 'POST':
        form = DateForm(request.post)
        if form.is_valid:
            form.save()
        return redirect('success')
    else:
        form = DateForm()
    return render(request, 'Date/cabinet.html', {'form': form})

def success(request):
    return HttpResponse('Данные успешно добавлены')