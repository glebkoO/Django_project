from django.forms import ModelForm
from .models import *

class DeskForm(ModelForm):
    class Meta:
        model = Desk
        fields = '__all__'
