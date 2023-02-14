from django import forms
from .models import *


class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = '__all__'