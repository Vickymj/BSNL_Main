from django.shortcuts import render
from app.models import Project
from app.models import Newbooking
from django.contrib.auth.models import User


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
 
def login(request):
    if request.method == 'POST':
        membername = request.POST.get('membername')
        moblieno = request.POST.get('moblieno')

        # Query the register table for a matching name
        try:
            detail = Newbooking.objects.get(membername=membername,password=password)
        except Newbooking.DoesNotExist:
            error_message = 'Invalid username or password'
            return render(request, 'second/login.html', {'error_message': error_message})

        if detail.moblieno == moblieno:
            # Passwords match, perform successful login
            return render(request, 'second/home.html')
        else:
            # Incorrect password
            error_message = 'Invalid username or password'
            return render(request, 'second/login.html', {'error_message': error_message})
    else:
        # GET request method used
        return render(request, 'second/login.html')
