from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all() 
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks' : tasks, 'form' : form}
    return render(request, 'tasks/index.html' , context)

def updateTask(request, pk):
    # Creating a form to change an existing article.
    tasks = Task.objects.get(id = pk) #all tasks get id
    form = TaskForm(instance = tasks) #prefill the form 

    if request.method == 'POST':
        form = TaskForm(request.POST, instance = tasks) #updating the old task with the new one
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'form' : form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request,pk):
    item = Task.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item' : item}
    return render(request,'tasks/delete.html', context)



