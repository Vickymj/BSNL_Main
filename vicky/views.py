from django.shortcuts import render, HttpResponse
from .models import Test

# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         dbmodel = Test()
#         dbmodel.name = request.POST.get('username')
#         dbmodel.password = request.POST.get('password')
#         dbmodel.save()
#     return render(request, 'vickyindex.html')


def index(request):
    dbmodel = Test.objects.all()
    return render(request, 'vickyindex.html',{'dbmodel':dbmodel})