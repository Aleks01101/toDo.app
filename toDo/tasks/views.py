from django.shortcuts import render
from .models import *


def index(request):
    tasks = Task.object.all()
    context = {'tasks' : tasks}
    return render(request, 'tasks/index.html')


