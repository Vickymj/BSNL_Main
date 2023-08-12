from django.shortcuts import render
from app.models import Project

# Create your views here.
def index(request):
    data = Project.objects.all()
    context={
        "data":data
    }
    return render(request,'page/home.html', {"data": data})

def contact(request):
    return render(request, 'page/contact.html')
def project(request):
    data = Project.objects.all()
    context={
        "data":data
    }
    
    return render(request, 'page/projects.html', {"data": data})
def services(request):
    return render(request, 'page/services.html')
def gallery(request):
    return render(request, 'page/gallery.html')
def board(request):
    return render(request, 'page/board.html')
def signin(request):
    return render(request,'page/login/signin.html')
def about(request):
    return render(request,'page/about.html  ')
def test(request):
    return render(request,'page/customer/home.html')
