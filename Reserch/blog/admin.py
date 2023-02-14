from django.contrib import admin
from .models import Desk
# Register your models here.
class DeskAdmin(admin.ModelAdmin):
    list_display = ('title', 'context')
    list_display_links = ('title',)
    search_fields = ('id', 'date')
admin.site.register(Desk, DeskAdmin)