from datetime import datetime
from django.shortcuts import render
from name.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"index.html")

def servies(request):
    return render(request,"servies.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        text=request.POST.get('text')

        contact=Contact(name=name,email=email,phone=phone,text=text,time=datetime.now())
        contact.save()
        messages.success(request, 'Your conctact form is successfully Submit!')
        

    return render(request,"contact.html")  #password :-- lala123+-*/

