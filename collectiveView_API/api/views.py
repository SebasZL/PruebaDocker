from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'form.html')

def elevar(request):
    num = int(request.GET["num"])
    res = num * num
    return render(request,'result.html', {"result": res})