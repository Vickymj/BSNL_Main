from django.shortcuts import render
from app.models import Project
from app.models import Newbooking
# Create your views here.

def home(request):
    return render(request,'page/customer/home.html')
def product(request):
    return render(request,'page/customer/product.html')