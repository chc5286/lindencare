from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import DetailView
from django.shortcuts import render

from .models import Task

def index(request):
    task_list = Task.objects
    context = {'task_list': task_list}
    return render(request,'tasks/index.html',context)

