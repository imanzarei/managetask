from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from tasks.form import MakeForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework import status
from django.db.models import Q


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


def login_required_api(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Unauthorized'}, status=401)
        return view_func(request, *args, **kwargs)

    return wrapper


@login_required_api
@api_view(['GET'])
def task_list(request):
    search_term = request.GET.get('search', '')
    # Filter tasks based on title or description containing the search term
    items = Task.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))
    serializer = TaskSerializer(items, many=True)
    return Response(serializer.data)


@login_required_api
@api_view(['POST'])
def create_task(request):
    mutable_data = request.data.copy()  # Create a mutable copy of the QueryDict
    mutable_data['created_by'] = request.user.id  # Set the 'created_by' field with the current user's ID

    serializer = TaskSerializer(data=mutable_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required_api
@api_view(['PUT'])
def update_task(request, pk):
    item = Task.objects.get(pk=pk)
    new_data = request.data.copy()  # Create a copy of the request data
    new_data.pop('created_by', None)  # Exclude the 'created_by' field from the update

    serializer = TaskSerializer(instance=item, data=new_data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)  # Print the serialization errors in the console for debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required_api
@api_view(['DELETE'])
def delete_task(request, pk):
    item = Task.objects.get(pk=pk)
    item.delete()
    return Response(status=204)
