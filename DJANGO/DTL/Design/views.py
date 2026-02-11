from django.shortcuts import render
from django.http import HttpResponse 

def hello(request):
    # return HttpResponse("<h1>Welcome!</h1>")
    return render(request,'home.html',{'name':'Python - Django'})

def add(request):
    value_1 = int(request.POST['number 1']) # POST, GET
    value_2 = int(request.POST['number 2'])
    res = value_1 + value_2
    return render(request,'result.html',{'result':res})
