from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello, World!")
    return render(request,'hello/index.html')


def dedar(request):
    return HttpResponse("Hello, Dedar!")


def greet(request, name):
    #return HttpResponse(f"Hello, {name}")
    return render(request, 'hello/greet.html',{
        "name": name.capitalize()
    })