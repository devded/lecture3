from datetime import date
from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.
def index(request):
    #return HttpResponse("New Year")
    now = datetime.datetime.now();
    return render(request,'newyear/index.html',{
        "newyear" : now.day == 1 and now.month == 1
    })