from django.shortcuts import render, redirect
from .models import UserTask, Taskmodel, Taskcomment
from .forms import PostForm

def taskpush(request):
    user_task = UserTask.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Homepage')
    else:
        form = PostForm()
    return render(request, 'index.html', {
        'form': form,
        'user_task' :user_task,
        })

