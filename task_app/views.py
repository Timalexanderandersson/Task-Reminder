from django.shortcuts import render
from .models import UserTask, Taskmodel, Taskcomment


def Userforviews(request):
    user = Taskmodel.objects.all()
    user_task = UserTask.objects.all()
    task_comment = Taskcomment.objects.all()

    return render(request, 'index.html', {
        'user': user,
        'user_task': user_task,
        'task_comment': task_comment,
        })