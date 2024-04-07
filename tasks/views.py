from apis.models import Task
from django.shortcuts import render, redirect, get_object_or_404
from tasks.form import MakeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_page(request):
    error_message = None  # Initialize error message variable

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('task_list_page')  # Redirect to the task list page after successful login
        else:
            # Set error message for invalid credentials
            error_message = 'Invalid username or password. Please try again.'

    return render(request, 'tasks/login.html', {'error_message': error_message})


def logout_page(request):
    logout(request)
    return redirect('login_page')  # Redirect to the login page after logout


@login_required
def task_list_page(request):
    return render(request, 'tasks/task_list.html')


@login_required
def task_delete_page(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_delete.html', {'task': task})


@login_required
def task_detail_page(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = MakeForm(instance=task)
    return render(request, 'tasks/task_detail.html', {'form': form, 'task': task})


@login_required
def task_form_page(request):
    form = MakeForm()
    return render(request, 'tasks/task_form.html', {'form': form})


