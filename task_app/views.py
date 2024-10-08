from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView, UpdateView
from .models import TaskUser
from .forms import PostUser, SigningUp, SignIn, ContactForms, PostUserFirst
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required


def homepage(request):
    '''
    Function for redirection when entering the website.
    If the user is authenticated, redirect to task-create.
    If not authenticated, send to index.html.
    '''
    if request.user.is_authenticated:
        return redirect('task-create')
    return render(request, 'index.html')


@login_required
def search_here(request):
    '''
    Search function to find tasks in the list.

    allinfo shows the found tasks.
    searching is for collecting data from the input.
    If search = checking for text in input is empty, and message if it's empty.
    If allinfo.exists() == False check if task exists.
    If task does not exist it shows the message 'No task with this name.'
    '''
    form = PostUser(request.POST)
    allinfo = TaskUser.objects.filter(user=request.user)
    searching = request.GET.get('search-text').strip()
    if searching == '':
        messages.error(request, 'Search for a task')
        return redirect('task-create')
    allinfo = allinfo.filter(title__icontains=searching)
    if not allinfo.exists():
        messages.error(request, 'No task with this name.')
        return redirect('task-create')

    return render(request, 'task_edit.html', {
        'form': form,
        'allinfo': allinfo,
    })


# Adding to the task list as user.
@login_required
def taskpush(request):
    '''
    Function for adding tasks into a list.

    allinfo shows the tasks and sort them.
    Form PostUser shows form with 'title', 'description', 'completed',
    'due_date', 'time_date'. Shows you message if valid 'You added a task.'
    Otherwise 'Did not fill in all.' message appears.
    '''
    alinfo = TaskUser.objects.filter(user=request.user).order_by('-created_at')

    if request.method == 'POST':
        form = PostUserFirst(request.POST)
        if form.is_valid():
            tasks = form.save(commit=False)
            tasks.user = request.user
            tasks.save()
            messages.success(request, 'You added a task.')
            return redirect('task-create')
        else:
            messages.error(request, 'Did not fill in all.')
    else:
        form = PostUserFirst()

    return render(request, 'task_edit.html', {
        'form': form,
        'allinfo': alinfo,
    })


# Delete tasks.
class DeleteTask(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TaskUser
    context_object_name = 'tasks'
    template_name = 'delete_site.html'
    success_url = reverse_lazy('task-create')
    success_message = 'Deleted the task'


# Updating tasks
class UpdateTask(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TaskUser
    form_class = PostUser
    template_name = 'edit_task.html'
    context_object_name = 'tasks'
    success_message = 'Updated task'
    success_url = reverse_lazy('task-create')


def signing_up(request):
    '''
    Function for signing up to the webpage.

    This function handles all registration for a new user to get access to
    the website. The form shows 'username', 'email', 'password1',
    'password2'. It saves the user and redirect to the task-create and shows
    message 'Welcome {user.username} to your account.'
    '''
    if request.method == 'GET':
        form = SigningUp()
    else:
        form = SigningUp(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = user.username.lower()
            user.save()
            messages.success(request, f'hey {user.username} to your account')
            login(request, user)
            return redirect('task-create')

    return render(request, 'register.html', {'form': form})


def accountlogin(request):
    '''
    Function for user to sign in.

    If the user is authenticated, it gets sent back to task-create.
    If the user is not authenticated, it gets sent to login.html.
    Form shows 'username', 'password'.
    '''
    if request.user.is_authenticated:
        return redirect('task-create')

    if request.method == 'GET':
        form = SignIn()
        return render(request, 'login.html', {'form': form})

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
        messages.error(request, 'Wrong username or password')
        return render(request, 'login.html', {'form': form})


@login_required
def accountlogout(request):
    '''
    Function for sign out.

    This function handles the sign out of the user.
    If signed out, redirect to Homepage/index.html.
    '''
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You signed out successfully.')
        return redirect('Homepage')

    return render(request, 'logout.html')


def contact_form(request):
    '''
    Function that sends the contact form.
    Then sends the user to form_success webpage.
    '''
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_success')
    else:
        form = ContactForms()

    return render(request, 'contact.html', {'form': form})


def form_success(request):
    '''
    Function that renders visitor/user the successfully submitted webpage.
    '''
    return render(request, 'email_sent.html')
