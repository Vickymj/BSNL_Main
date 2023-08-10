from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'page/home.html')
def contact(request):
    return render(request, 'page/contact.html')
def project(request):
    return render(request, 'page/projects.html')
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