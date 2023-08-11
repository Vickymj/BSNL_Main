from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Newbooking,Family,Project
from .forms import NewbookingForm,ProjectForm
from django.contrib import messages
# Create your views here.
def home(request):
	return render(request,'site2/home.html')
def booksum(request):
	return render(request,'site2/dashboard/booksum.html')
def bss(request):
	return render(request,'site2/dashboard/bss.html')
# def newbooking(request):
#     if request.method == "POST":
#         form = NewbookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your account has been created. You can log in now!')
#             return HttpResponseRedirect('newbooking')
#     else:
#         form = NewbookingForm
#     return render(request, 'site2/addcredential/demo.html',{'form':form, })

def newbooking(request):
    if request.method == 'POST':
        form = NewbookingForm(request.POST)
        if form.is_valid():
            membername = form.cleaned_data['membername']
            fathername = form.cleaned_data['fathername']
            dob = form.cleaned_data['dob']
            age = form.cleaned_data['age']
            moblieno = form.cleaned_data['moblieno']
            alternateno = form.cleaned_data['alternateno']
            emailid = form.cleaned_data['emailid']
            address = form.cleaned_data['address']
            panno = form.cleaned_data['panno']
            aadhhaarno = form.cleaned_data['aadhhaarno']
            nomieename = form.cleaned_data['nomieename']
            nomieeage = form.cleaned_data['nomieeage']
            nomieerelationship = form.cleaned_data['nomieerelationship']
            nomieeaddress = form.cleaned_data['nomieeaddress']
            project = form.cleaned_data['project']
            dimension = form.cleaned_data['dimension']
            total = form.cleaned_data['total']
            downpayment = form.cleaned_data['downpayment']
            siterefer = form.cleaned_data['siterefer']
            modeofpay = form.cleaned_data['modeofpay']
            bank = form.cleaned_data['bank']
            branch = form.cleaned_data['branch']
            chequeno = form.cleaned_data['chequeno']
            paydate = form.cleaned_data['paydate']
            amount = form.cleaned_data['amount']
            seniorityno = form.cleaned_data['seniorityno']
            amno = form.cleaned_data['amno']
            receiptno = form.cleaned_data['receiptno']
            familymemname = form.cleaned_data['familymemname']
            familymemage = form.cleaned_data['familymemage']  # Add this line
            familymemrelation = form.cleaned_data['familymemrelation']            
            # Save to Test model
            test_instance = Newbooking(membername=membername,fathername=fathername,dob=dob,age=age,moblieno=moblieno,alternateno=alternateno,emailid=emailid,address=address,panno=panno,aadhhaarno=aadhhaarno,nomieename=nomieename,nomieeage=nomieeage,nomieerelationship=nomieerelationship,nomieeaddress=nomieeaddress,project=project,dimension=dimension,total=total,downpayment=downpayment,siterefer=siterefer,modeofpay=modeofpay,bank=bank,branch=branch,chequeno=chequeno,paydate=paydate,amount=amount,seniorityno=seniorityno,amno=amno,receiptno=receiptno)
            test_instance.save()

            # Save to Value model
            value_instance = Family(membername=test_instance,familymemname=familymemname,familymemage=familymemage,familymemrelation=familymemrelation)
            value_instance.save()

            return HttpResponse('/newbooking')
    else:
        form = NewbookingForm()

    return render(request,  'site2/addcredential/newbooking.html',{'form':form, })

def generate(request):
	return render(request,'site2/addcredential/generate.html')
def receipt(request):
	return render(request,'site2/receipts/receipts.html')
def login(request):
	return render(request,'site2/login/login.html')
def project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return HttpResponseRedirect('project')
    else:
        form = ProjectForm()
        messages.success(request, '. You can log in now!')
    return render(request,'site2/project/project.html',{'form':form, })
def project_view(request):
    data = Project.objects.all()
    context={
        "data":data
    }
    return render(request,'page/home.html', {"data": data})
