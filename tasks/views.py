from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import DetailView
from django.shortcuts import render

from .models import Task

def task_list(request):
    task_list = ['hi','go','do it']
    context = {'task_list': task_list}
    return render(request,'tasks/base.html',context)

