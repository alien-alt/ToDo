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
from users.views import HomeView, TasksView, DetailTasksView, CompletedTasksView, AddTaskView, RegisterView, LoginView, MakeRegisterView, MakeLoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('tasks/', TasksView.as_view(), name='tasks'),
    path('task-detail/', DetailTasksView.as_view(), name='task_detail'),
    path('completed-tasks', CompletedTasksView.as_view(), name='completed_tasks'),
    path('add-task', AddTaskView.as_view(), name='add_task'),
    path('make-register', MakeRegisterView.as_view(), name='make_register'),
    path('make-login', MakeLoginView.as_view(), name='make_login'),
    path('logout', LogoutView.as_view(), name='logout'),
]

