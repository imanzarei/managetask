from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import task_list_page, task_form_page, task_detail_page, task_delete_page, login_page, logout_page

urlpatterns = [
    path('accounts/login/', login_page, name='login_page'),  # Redirect /accounts/login to the login_page view
    path('accounts/logout/', logout_page, name='logout_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', task_list_page, name='task_list_page'),
    path('page/create', task_form_page, name='create_task_page'),
    path('page/detail/<int:pk>', task_detail_page, name='update_task'),
    path('page/delete/<int:pk>', task_delete_page, name='task_delete'),

]
