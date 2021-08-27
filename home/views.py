from django.shortcuts import render
from home.models import User

# Create your views here.
def home(request):
    if request.method == 'POST' :
        email = request.POST['email']
        password = request.POST['password']

    return render(request,"home.html")

def register(request):
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password == re_password:
            ins = User(name=name, email=email, address=address, password=password)
            ins.save()

    return render(request,"register.html")

def details(request):
    return render(request,"details.html")

def logout(request):
    return None