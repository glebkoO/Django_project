from django.contrib.auth.forms import UserCreationForm
from django.http import request
from django.shortcuts import render, redirect

from django.views.generic import ListView
from django.db.models import Q


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
        object_list = Date.objects.filter(Q(first_name__contains=query) | Q(last_name__contains=query))
        context = {'query': query, 'object_list': object_list}
    return render(request, 'Date/search_results.html', context)
# class SearchResultView(ListView):
#     model = Date
#     template_name = 'search_results.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('case')
#         if query in request.GET:
#             object_list = Date.objects.filter(Q(first_name__contains=query) | Q(last_name__contains=query))
#             return object_list

# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     template_name = 'Date/register.html'
#     success_url = reverse_lazy('login')
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Регистрация')
#         return dict(list(context.items()) + list(c_def.items()))
