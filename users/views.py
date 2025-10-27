from django.shortcuts import render
from django.views.generic import TemplateView, View

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class RegisterView(TemplateView):
    template_name = 'register.html'

class TasksView(TemplateView):
    template_name = 'tasks.html'

class DetailTasksView(TemplateView):
    template_name = 'task_detail.html'

class CompletedTasksView(TemplateView):
    template_name = 'completed_tasks.html'

class AddTaskView(TemplateView):
    template_name = 'add_task.html'

"""POST views"""

class MakeRegister(View):
    pass

