from django.contrib import admin
from . models import *
class DateAdmin(admin.ModelAdmin):
    list_display = ('created', 'first_name', 'last_name', 'age', )
    list_display_links = ('first_name', 'last_name')
    search_fields = ('id', 'date', 'first_name', 'last_name')

admin.site.register(Date, DateAdmin)
