from django.contrib import admin
from . models import *
class DateAdmin(admin.ModelAdmin):
    list_display = ('created', 'name', 'age', )
    list_display_links = ('name',)
    search_fields = ('id', 'date', 'name')

admin.site.register(Date, DateAdmin)
