from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView, UpdateView
from .models import TaskUser
from .forms import PostUser
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

#Takes user/visitor to the front page.
def homepage(request):

    return render(request, 'task_edit.html',)


# Adding to the task list as user.
def taskpush(request):
    allinfo = TaskUser.objects.filter()
    if request.method == 'POST':
            form = PostUser(request.POST)
            if form.is_valid():
               tasks = form.save(commit=False)
               tasks.user = request.user
               tasks.save()
               messages.success(request, f'You added a task.')
               return redirect('task_create')
            else:
                messages.error(request, 'Did not fill in all.')
    else:
            form = PostUser()
    return render(request, 'task_edit.html', {
        'form': form,
        'allinfo':allinfo,
        })

# Delete tasks.
class DeleteTask(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = TaskUser
    context_object_name = 'tasks'
    template_name = 'delete_site.html'
    success_url = reverse_lazy('task-create')
    success_message = 'Deleted the task'

#Updating tasks
class UpdateTask(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = TaskUser
    form_class = PostUser
    template_name = 'edit_task.html'
    context_object_name = 'tasks'
    success_message = 'Updated task'
    success_url = reverse_lazy('task-create')