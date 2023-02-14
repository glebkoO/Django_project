from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView

from .models import *
from .forms import *

def main(request):
    blog = Desk.objects.all()
    form = DeskForm()
    if request.method == 'POST':
        form = DeskForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/")
    else:
        form = DeskForm()
    return render(request, 'blog/main.html', {'form': form, 'blog': blog})
