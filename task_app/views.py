from django.shortcuts import render, redirect
from .models import UserTask
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



