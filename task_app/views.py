from django.shortcuts import render, redirect
from .models import UserTask, Taskmodel, Taskcomment
from .forms import PostForm, PostUser
from django.contrib import messages

# Views for adding to the task list.
def taskpush(request):
    models_task = Taskmodel.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Homepage')
    else:
        form = PostForm()

        return render(request, 'index.html', {
        'form': form,
        'models_task': models_task,
        })
