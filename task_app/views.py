from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView, UpdateView
from .models import TaskUser
from .forms import PostUser, SigningUp, SignIn
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

#Takes user/visitor to the front page.
def homepage(request):
    if request.user.is_authenticated:
        return redirect('task-create')
    return render(request, 'index.html',)


# Adding to the task list as user.
@login_required
def taskpush(request):
    allinfo = TaskUser.objects.filter(user=request.user).order_by('-created_at')
    if request.method == 'POST':
            form = PostUser(request.POST)
            if form.is_valid():
               tasks = form.save(commit=False)
               tasks.user = request.user
               tasks.save()
               messages.success(request, f'You added a task.')
               return redirect('task-create')
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

#Account sign up function
def signing_up(request):
    if request.method == 'GET':
        form = SigningUp()
    else:
        form = SigningUp(request.POST)
        if form.is_valid():
           user = form.save()
           user.username = user.username.lower()
           user.save()
           messages.success(request, f'Welcome {user.username} to your account.')
           login(request, user)
           return redirect('task-create')
               
    return render(request, 'register.html',{'form':form})

#Account sign in function
def AccountLogin(request):
    if request.user.is_authenticated:
        return redirect('task-create')
    if request.method == 'GET':
        form = SignIn()
        return render(request, 'login.html', {'form':form})
    
    elif request.method == 'POST':
        form = SignIn(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Welcome {username}.')
                return redirect('task-create')

        messages.error(request, f'Wrong username or password')
        return render(request, 'login.html', {'form':form})


#Sign out function
@login_required
def AccountLogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, f'You sign out.')
        return redirect('Homepage')
    return render(request,'logout.html')