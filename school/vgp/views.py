from django.shortcuts import render,redirect
from .models import data

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def program(request):
    return render(request,"program.html")
def save(request):
    name=request.POST['name']
    email=request.POST['email']
    mob_number=request.POST['mob_number']
    data.objects.create(name=name,email=email,mob_number=mob_number).save()
    return redirect('/contact')
