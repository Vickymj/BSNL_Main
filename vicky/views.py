from django.shortcuts import render, HttpResponse,redirect
from .models import Test,Value,Order
from .forms import TestForm,ValueForm,CombinedForm,OrderForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        dbmodel = Test()
        dbmodel.name = request.POST.get('username')
        dbmodel.password = request.POST.get('password')

        for username, password in zip(dbmodel.name, dbmodel.password):
            new_user = Test(name=username, password=password)
            new_user.save()
        dbmodel.save()
    return render(request, 'vickyindex.html')


def index1(request):
    dbmodel = Test.objects.all()
    return render(request, 'vickyindex.html',{'dbmodel':dbmodel})
def testing_db(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            value = form.cleaned_data['value']
            
            # Save to Test model
            test_instance = Test(name=name, password=password)
            test_instance.save()

            # Save to Value model
            value_instance = Value(name=test_instance, value=value)
            value_instance.save()

            return HttpResponse('done')
    else:
        form = CombinedForm()

    return render(request, 'template.html', {'form': form})

# def testing_db(request):
#         db1 = Test()
#         db1.name ='Vicky'
#         db1.password = 'vike@123'
#         db1.save()
#         db2 = Value()
#         db2.name_id=db1.id
#         db2.value = 'tech'
#         db2.save()
#         return HttpResponse('done')

# def customer_details(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         customers = Test.objects.filter(name=name)
        
#         if customers.exists():
#             # You can choose which customer to display, for example the first one
#             customer = customers.first()
#             return render(request, 'details.html', {'customer': customer})
#         else:
#             return render(request, 'details.html', {'customer': None})
    
#     return render(request, 'search.html')

# def create_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             customer_name = form.cleaned_data['customer_name']
#             order_date = form.cleaned_data['order_date']
#             product_name = form.cleaned_data['product_name']
#             quantity = form.cleaned_data['quantity']

#             customer = Test.objects.get(name=customer_name)

#             order = Order(customer=customer, order_date=order_date, product_name=product_name, quantity=quantity)
#             order.save()

#             return render(request, 'details.html', {'order': order})
#     else:
#         form = OrderForm()

#     return render(request, 'search.html', {'form': form})

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist


def customer_details(request):
    selected_customer = None
    order_created = False
    matching_customers = []

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'search_customer':
            name = request.POST.get('name')
            customers = Test.objects.filter(name=name)

            if customers.exists():
                matching_customers = customers

        elif action == 'create_order':
            name = request.POST.get('name')
            order_date = request.POST.get('order_date')
            product_name = request.POST.get('product_name')
            quantity = request.POST.get('quantity')

            try:
                customer_id = request.POST.get('customer_id')
                customer = Test.objects.get(id=customer_id)

                # Create a new order instance
                order = Order(name=customer, order_date=order_date, product_name=product_name, quantity=quantity)
                order.save()
                order_created = True

            except Test.DoesNotExist:
                customer = None

    return render(request, 'search.html', {'selected_customer': selected_customer, 'order_created': order_created, 'matching_customers': matching_customers})
