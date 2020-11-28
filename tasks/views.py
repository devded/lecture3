import tasks
from django.shortcuts import render
from django.http import HttpResponse
from django import forms


# Create your views here.

app_name = "tasks"
mylists = ["apple", "banana", "cherry"]
def index(request):
    #return HttpResponse('Tasks')
    
    tasks = {
        'name': "Dedar Alam",
        'lists': mylists
    }
    return render(request,'tasks/index.html', tasks);



def add(request):
    if request.method == "POST":
        form = request.POST.dict()
        name = form.get("name")
        #return HttpResponse(name)
        mylists.append(name)

        tasks = {
            'name': "Dedar Alam",
            'lists': mylists
        }
        return render(request,'tasks/index.html', tasks);
    else:
        return render(request, 'tasks/add.html');