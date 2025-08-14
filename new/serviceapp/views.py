from django.shortcuts import render,HttpResponse
from . models import Role, Location

# Create your views here.
def first(request):
    return HttpResponse("avinash")


def signup(request):
    return render(request,"signup.html")    
