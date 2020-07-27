from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2>Welcome to Views of MYAPP</h2>")

def home(request):
    return render(request,"myapp/home.html",{'name':'Sunil'})

def base(request):
    return render(request,"myapp/base.html")

def child(request):
    return render(request,"child.html")