from django.shortcuts import render
from .models import Task


# Create your views here.

def add(request):
    

    if request.method == "POST":
        nam = request.POST.get('name','')
        passcod = request.POST.get('passcode','')

        task = Task(name=nam,passcode=passcod)
        task.save()
    return render(request,'myapp/add.html')

def main(request):
    return render(request,'myapp/main.html')
