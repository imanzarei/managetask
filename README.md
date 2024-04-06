# Task Management

## Description
This Django project implements views for task management, and API endpoints for tasks. 

## Views

1. **Login Page View**
    - Path: /accounts/login/
    - Function: `login_page(request)`
    - Description: Handles user login functionality. Displays an error message for invalid credentials.

2. **Logout Page View**
    - Path: /accounts/logout/
    - Function: `logout_page(request)`
    - Description: Logs out the current user and redirects to the login page.

3. **Task List Page View**
    - Path: /
    - Function: `task_list_page(request)`
    - Description: Renders the task list page for authenticated users.

4. **Task Delete Page View**
    - Path: /page/detail/<int:pk>
    - Function: `task_delete_page(request, pk)`
    - Description: Renders the task delete page for a specific task identified by the primary key (pk).

5. **Task Detail Page View**
    - Path: /page/detail/<int:pk>
    - Function: `task_detail_page(request, pk)`
    - Description: Renders the task detail page for a specific task identified by the primary key (pk).

6. **Task Form Page View**
    - Path: /page/create
    - Function: `task_form_page(request)`
    - Description: Renders the task form page for creating a new task.

7. **API View - Task List**
    - Path: /list/
    - Function: `task_list(request)`
    - Description: API endpoint for listing tasks based on a search term.

8. **API View - Create Task**
    - Path: /create/
    - Function: `create_task(request)`
    - Description: API endpoint for creating a new task.

9. **API View - Update Task**
    - Path: /update/<int:pk>/
    - Function: `update_task(request, pk)`
    - Description: API endpoint for updating an existing task identified by the primary key (pk).

10. **API View - Delete Task**
    - Path: /delete/<int:pk>/
    - Function: `delete_task(request, pk)`
    - Description: API endpoint for deleting a task identified by the primary key (pk).

## URLs

- URL patterns are defined in the `urlpatterns` list in the project's URL configuration file.
- Main url : http://localhost:8000/task/ if it is not authenticated, redirect it to the Login page.

### Run Test
- For running the test run: `python3 manage.py test tasks`

### Installation
1. Set up a Python virtual environment.
2. Install project dependencies using `pip install -r requirements.txt`.
3. Run migrations with `./manage.py migrate`.
4. Start the Django development server with `./manage.py runserver`.