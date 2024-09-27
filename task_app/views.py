from django.shortcuts import render, redirect
from .models import TaskUser
from .forms import PostUser
from django.contrib import messages

#Takes user/visitor to the front page.
def homepage(request):

    return render(request, 'task_edit.html',)


# Views for adding to the task list.
def taskpush(request):
    form = PostUser(request.POST)
    allinfo = TaskUser.objects.filter()
    if request.method == 'POST':
        form = PostUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Homepage')
    else:
        form_user = PostUser()
        return render(request, 'task_edit.html', {
        'form': form,
        'allinfo': allinfo,
        })



