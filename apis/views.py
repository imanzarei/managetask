from apis.models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.db.models import Q
from django.core.exceptions import PermissionDenied


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
    try:
        item = Task.objects.get(pk=pk)
        if item.created_by != request.user:
            raise PermissionDenied("You do not have permission to update this task.")

        new_data = request.data.copy()  # Create a copy of the request data
        new_data.pop('created_by', None)  # Exclude the 'created_by' field from the update

        serializer = TaskSerializer(instance=item, data=new_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)


@login_required_api
@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        item = Task.objects.get(pk=pk)
        if item.created_by != request.user:
            raise PermissionDenied("You do not have permission to delete this task.")

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
