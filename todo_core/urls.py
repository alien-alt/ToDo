"""
URL configuration for todo_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import (
        # GET views
        AddTaskView,HomeView, TasksView, DetailTasksView, 
        CompletedTasksView, DetailCompletedTasksView, 
        RegisterView, LoginView,
        # POST views
        MakeRegisterView, MakeLoginView,
        LogoutView, CreateTaskView, 
        EditTaskView, CompleteTask, 
        DeleteTaskView
        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('tasks/', TasksView.as_view(), name='tasks'),
    path('task-detail/<int:id>/', DetailTasksView.as_view(), name='task_detail'),
    path('completed-tasks', CompletedTasksView.as_view(), name='completed_tasks'),
    path('detail-completed-task/<int:id>', DetailCompletedTasksView.as_view(), name='detail_completed_task'),
    path('add-task', AddTaskView.as_view(), name='add_task'),
    # POST views
    path('make-register', MakeRegisterView.as_view(), name='make_register'),
    path('make-login', MakeLoginView.as_view(), name='make_login'),
    path('create_task', CreateTaskView.as_view(), name='create_task'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('edit_task', EditTaskView.as_view(), name='edit_task'),
    path('complete-task', CompleteTask.as_view(), name='complete_task'),
    path('delete-task', DeleteTaskView.as_view(), name='delete_task'),
]

