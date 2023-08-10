from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Newbooking
from .forms import NewbookingForm
from django.contrib import messages
# Create your views here.
def home(request):
	return render(request,'site2/home.html')
def booksum(request):
	return render(request,'site2/dashboard/booksum.html')
def bss(request):
	return render(request,'site2/dashboard/bss.html')
def newbooking(request):
    if request.method == "POST":
        form = NewbookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return HttpResponseRedirect('newbooking')
    else:
        form = NewbookingForm
    return render(request, 'site2/addcredential/demo.html',{'form':form, })
def generate(request):
	return render(request,'site2/addcredential/demo1.html')
def receipt(request):
	return render(request,'site2/receipts/receipts.html')
def login(request):
	return render(request,'site2/login/login.html')
def project(request):
    return render(request,'site2/project/project.html')