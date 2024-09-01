from django.shortcuts import render
from django.views import generic
from .models import UserTask, Taskmodel, Taskcomment


def Userforviews(request):
    user = Taskmodel.objects.all()
    user_task = UserTask.objects.all()
    task_comment = Taskcomment.objects.all()
    template_name = "task_app/index.html"

    return render(request, 'index.html', {
        'user': user,
        'user_task': user_task,
        'task_comment': task_comment,
        })