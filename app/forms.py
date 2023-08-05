from django import forms
from django.forms import ModelForm
from .models import Newbooking

class NewbookingForm(forms.ModelForm):
	class Meta:
		model = Newbooking
		fields = '__all__'