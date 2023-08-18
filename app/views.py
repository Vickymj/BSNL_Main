from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Newbooking,Family,Project,Receipt,Role
from .forms import NewbookingForm,ProjectForm,ReceiptForm,SearchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login

# Create your views here.
def home1(request):
	return render(request,'site2/home.html')
def booksum(request):
	return render(request,'site2/dashboard/booksum.html')
def bss(request):
	return render(request,'site2/dashboard/bss.html')

def newbooking(request):
    if request.method == 'POST':
        form = NewbookingForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
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
            role=form.cleaned_data['role']   
            # user model
            user_instance = User(username=username,last_name=fathername,email=emailid) 
            user_instance.save()       
            # Save to Test model
            test_instance = Newbooking(username=user_instance, dob=dob, age=age, moblieno=moblieno, alternateno=alternateno, address=address, panno=panno, aadhhaarno=aadhhaarno, nomieename=nomieename, nomieeage=nomieeage, nomieerelationship=nomieerelationship, nomieeaddress=nomieeaddress, project=project, dimension=dimension, total=total, downpayment=downpayment, siterefer=siterefer, modeofpay=modeofpay, bank=bank, branch=branch, chequeno=chequeno, paydate=paydate, amount=amount, seniorityno=seniorityno, amno=amno, receiptno=receiptno)
            test_instance.save()
            # Save to Value model
            value_instance = Family(username=test_instance,familymemname=familymemname,familymemage=familymemage,familymemrelation=familymemrelation)
            value_instance.save()
            # Save to Role
            role_instance = Role(username=user_instance,role=role)
            role_instance.save()

            return HttpResponse('/newbooking')
    else:
        form = NewbookingForm()

    return render(request,  'site2/addcredential/newbooking.html',{'form':form, })

def generate(request):
    selected_customer = None
    order_created = False
    matching_customers = []
    username = None 

    if request.method == 'POST':

        action = request.POST.get('action')
        print('aution:',action)

        if action == 'search_customer':
            seniorityno = request.POST.get('search_membername')
            

            customers = Newbooking.objects.filter(seniorityno=seniorityno)

            if customers.exists():
                matching_customers = customers

        elif action == 'create_order':
            bank = request.POST['bank']
            print(bank)
            return HttpResponse('done')
            # customer = Newbooking.objects.get(seniorityno=seniorityno)
    
           
            # username = request.POST.get('username')
            # seniorityno = seniorityno
            # amount = request.POST.get('amount')
            # modeofpay = request.POST.get('modeofpay')
            # chequeno = request.POST.get('chequeno')
            # bank = request.POST.get('bank')
            # branch = request.POST.get('branch')
            # paydate = request.POST.get('paydate')
            # paystatus = request.POST.get('paystatus')
            # dateofreceipt = request.POST.get('dateofreceipt')

            # try:
            #     customer = Newbooking.objects.get(seniorityno=123)
            #     print('cust',customer)

            #     # Create a new order instance
            #     order = Receipt(
            #         username=username,
            #         seniorityno=customer,
            #         amount=amount,
            #         modeofpay=modeofpay,
            #         chequeno=chequeno,
            #         bank=bank,
            #         branch=branch,
            #         paydate=paydate,
            #         paystatus=paystatus,
            #         dateofreceipt=dateofreceipt
            #     )
            #     print('or:',order)
            #     order.save()
            #     order_created = True

            # except Newbooking.DoesNotExist:
            #     print('faile')

    return render(request, 'site2/addcredential/generate.html', {'selected_customer': selected_customer, 'order_created': order_created, 'matching_customers': matching_customers})

def create_receipt(request):
     if request.method == 'POST':
          amount = request.POST.get('amount')
          print(amount)
          return HttpResponse('done')
          
def receipt(request):
    data = Receipt.objects.all()
    context={
        "data":data
    }
    return render(request,'site2/receipts/receipts.html', {"data": data})
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username , password = password)
        if user is not None:
            auth_login(request, user)
            user_profile = User.objects.get('role')
            if user_profile.role == 'admin':
                return redirect('home1')
            else:
                return redirect('home')
        else:
            print("someone tried to login and falied!")
            print("Username : {} and Password : {}".format(username,password))
            return HttpResponse("Invalid credentials!")
    else:
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
def update_data(request, id):
    venue = Receipt.objects.get(id=id)
    form = ReceiptForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('receipt')
    return render(request,'site2/receipts/update_data.html',{'venue':venue,
                                                'form':form})

def delete_data(request, id):
        data = Receipt.objects.get(pk=id)
        data.delete()
        return redirect('receipt') 

def confirmletter(request):
    return render(request,'site2/receipts/confirmleter.html')    