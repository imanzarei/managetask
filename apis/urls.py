from django.urls import path
from .views import task_list, create_task, update_task, delete_task

urlpatterns = [
    path('list/', task_list),
    path('create/', create_task),
    path('update/<int:pk>/', update_task),
    path('delete/<int:pk>/', delete_task),
]