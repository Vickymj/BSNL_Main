from django.shortcuts import render, HttpResponse,redirect
from .models import Test,Value
from .forms import TestForm,ValueForm,CombinedForm
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
