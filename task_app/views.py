from django.shortcuts import render
from django.views import generic
from .models import UserTask

class TaskListAll(generic.ListView):
    queryset = UserTask.objects.all()
    template_name = "task_list_here.html"