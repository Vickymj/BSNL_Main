from django import forms
from django.forms import ModelForm
from .models import Test ,Value

class TestvalueForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name']

        value = forms.CharField(max_length=120)