from django.shortcuts import render, HttpResponse
from .models import Test

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
def value(request):
    if request.method == 'POST':
        form = TestvalueForm(request.POST)
        if form.is_valid():
            name = form.save()  # Save parent data

            value = form.cleaned_data['value']
            Value.objects.create(name=name, value=value)  # Save child data with foreign key
            
            return redirect('success')  # Redirect to a success page
    else:
        form = TestvalueForm()
    
    return render(request, 'your_template.html', {'form': form})