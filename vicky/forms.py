from django import forms
from django.forms import ModelForm
from .models import Test ,Value

# class TestForm(forms.ModelForm):
#     class Meta:
#         model = Test
#         fields = '__all__'

# class ValueForm(forms.ModelForm):
#     class Meta:
#         model = Value
#         fields = '__all__'
# class TestValueForm(forms.ModelForm):
#     class Meta:
#         model = Test 
#         fields = '__all__'
# class TestvalueForm(forms.ModelForm):
#     class Meta:
#         model = Value  # Using the Value model for the form
#         fields = '__all__'
class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'password']

class ValueForm(forms.ModelForm):
    class Meta:
        model = Value
        fields = ['name', 'value']
class CombinedForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    value = forms.CharField(max_length=100)