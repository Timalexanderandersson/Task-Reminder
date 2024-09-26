from django.shortcuts import render, redirect, get_object_or_404 
from .models import UserTask, Taskmodel, Taskcomment
from .forms import PostForm, PostUser
from django.contrib import messages

#Takes user/visitor to the front page.
def homepage(request):

    return render(request, 'index.html',)


# Views for adding to the task list.
def taskpush(request):
    models_task = Taskmodel.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        form_user = PostUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Homepage')
    else:
        form = PostForm()
        form_user = PostUser()
        return render(request, 'index.html', {
        'form': form,
        'models_task': models_task,
        'form_user': form_user,
        })

def newpage(request,task_id):
    show_title = get_object_or_404(Taskmodel, id=task_id)
    models_task = Taskmodel.objects.all()
    user_models = UserTask.objects.all()
    if request.method == 'POST':
        form_user = PostUser(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect('newpage', task_id=task_id)
    else:
        form_user = PostUser()
        return render(request, 'task_edit.html', {
        'models_task': models_task,
        'form_user': form_user,
        'user_models':user_models,
        'show_title':show_title,
        })

#Delete function for task list
def delete_task_list(request, task_id):
    delete_task = get_object_or_404(Taskmodel, id=task_id)
    delete_task.delete()
    return redirect('Homepage')


