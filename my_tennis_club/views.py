from django.shortcuts import render
from django.http import HttpResponse
from myfirstapp.models import todo

def home(request):
    return render(request,'index.html')


def formSubmit(request):
    if request.method == 'GET':
        task = request.GET['task']
        desc = request.GET['desc']
        data=todo.objects.create(task=task,desc=desc)
        data.save()
        return render(request,'index.html')

