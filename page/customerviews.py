from django.shortcuts import render,get_object_or_404,HttpResponse
from app.models import Project,Receipt,User,Role
from django.contrib.auth.decorators import login_required
from app.models import Newbooking
from django.http import FileResponse
from django.views.generic import View
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
@login_required
def home(request):
    return render(request,'page/customer/home.html')

# def product(request, username_id):
#     # Retrieve the logged-in user
#     logged_in_user = request.user
#     # Retrieve the Receipt instance using the username_id (assuming username_id is for Receipt)
#     receipt = get_object_or_404(Newbooking,  username=logged_in_user)
#     pill=get_object_or_404(Receipt,pk=username_id)
    
#     role = get_object_or_404(Role, username=logged_in_user)
#     # Retrieve related Newbooking instance from the receipt
#     newbooking = receipt.username  # You need to define the actual relation name

#     # Extract the fields you need
#     username = logged_in_user.username
#     dateofreceipt = receipt.dob
#     projectname=receipt.project
#     user_role = role.role  # Assuming user's role is stored in the user model

#     # Your view logic here...

#     return render(request, 'page/customer/product.html', {
#         'username': username,
#         'projectname':projectname,
#         'dateofreceipt': dateofreceipt,
#         'user_role': user_role,
#         # Other data as needed
#     })

def product(request):
    user = request.user
    rec = Receipt.objects.filter(username=user.username)
    for r in rec:
        print(r.username)
    return render(request,'page/customer/product.html',{'user':user})

def payment(request):
    return render(request,'page/customer/payment.html')
def pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=letter)
    textob =c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica",14)

    lines =[
        'this qmmmmm'
    ]
    for line in lines:
        textob.textLine(line)
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True,filename='text.pdf')