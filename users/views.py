from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import User, Task, CompletedTask
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    # Провереям авторизован ли пользователь
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        return redirect('register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username

        return context



class RegisterView(TemplateView):
    template_name = 'register.html'



class LoginView(TemplateView):
    template_name = 'login.html'



class TasksView(TemplateView):
    template_name = 'tasks.html'

    # Провереям авторизован ли пользователь
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        return redirect('register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        context['task_list'] = user.tasks.all()

        return context



class DetailTasksView(TemplateView):
    template_name = 'task_detail.html'

    # Провереям авторизован ли пользователь
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        return redirect('register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_id = self.kwargs.get('id')
        task_is_exists = self.request.user.tasks.filter(id=task_id).exists()

        if not(task_is_exists):
            return redirect('home')

        task = self.request.user.tasks.get(id=task_id)
        context = {'task': task}
        return context



class CompletedTasksView(TemplateView):
    template_name = 'completed_tasks.html'

    # Провереям авторизован ли пользователь
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        return redirect('register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        completed_tasks = self.request.user.completed_tasks.all()

        context = {'completed_tasks': completed_tasks}

        return context



class DetailCompletedTasksView(TemplateView):
    template_name = 'completed_task_detail.html'

    # Провереям авторизован ли пользователь
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        return redirect('register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        completed_task_id = self.kwargs.get('id')
        comleted_task_is_exists = self.request.user.completed_tasks.filter(id=completed_task_id).exists()

        if comleted_task_is_exists:
            completed_task = self.request.user.completed_tasks.get(id=completed_task_id)
            context = {'completed_task': completed_task}
            return context



class AddTaskView(TemplateView):
    template_name = 'add_task.html'



"""POST views"""
class MakeRegisterView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST

        username = data.get('username')
        password = data.get('password')

        is_fields_not_empty =  username and password
        is_username_unique = not(User.objects.filter(username=username).exists())


        if is_fields_not_empty and is_username_unique:
            new_user = User.objects.create_user(username=username, 
                                                password=password)

            login(request, new_user)
            return redirect('home')

        elif not(is_fields_not_empty):
            context = {'error': "Поля не должны быть пустыми"}
            return render(request, 'register.html', context)

        else:
            context = {'error': f"Имя {username} уже занято"}
            return render(request, 'register.html', context)



class MakeLoginView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST

        username = data.get('username')
        password = data.get('password')

        is_fields_not_empty =  username and password

        if is_fields_not_empty:

            user_is_exists = User.objects.filter(username=username).exists()

            if user_is_exists:
                user = User.objects.get(username=username)

                if check_password(password, user.password):
                    login(request, user)
                    print("\nLOGIN\n")
                    return redirect('home')

        return redirect('login')



class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('register')



class CreateTaskView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('register')

        data = request.POST
        name = data.get('title')
        description = data.get('description')
        priorety = data.get('priorety')

        if priorety == 'low':
            priorety = 0

        elif priorety == 'medium':
            priorety = 1

        else:
            priorety = 2

        new_task = Task.objects.create(
            name=name,
            description=description,
            author = request.user,
            priorety=priorety
        )

        new_task.save()

        return redirect('tasks')



class EditTaskView(View):
    def post(self, request, *args, **kwargs):
        if not(request.user.is_authenticated):
            return redirect('register')

        data = request.POST
        new_name = data.get('name')
        new_description = data.get('description')
        new_priorety = data.get('priorety')
        task_id = data.get('task_id')

        if not(request.user.tasks.filter(id=task_id).exists()):
            return redirect('home')

        task = request.user.tasks.get(id=task_id)

        task.name = new_name
        task.description = new_description
        task.priorety = new_priorety
        task.save()

        return redirect('tasks')



class CompleteTask(View):
    def post(self, request, *args, **kwargs):
        if not(request.user.is_authenticated):
            return redirect('register')

        task_id = request.POST.get('task_id')
        task_is_exists = request.user.tasks.filter(id=task_id).exists()

        if task_is_exists:
            task = request.user.tasks.get(id=task_id)
            completed_task = CompletedTask
            completed_task.objects.create(
                name = task.name,
                description = task.description,
                priorety = task.priorety,
                author = task.author
            )

            task.delete()

            return redirect('completed_tasks')

        return redirect('tasks')



class DeleteTaskView(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')

        if not(request.user.is_authenticated):
            return redirect('register')

        if not(request.user.tasks.filter(id=task_id).exists()):
            return redirect('home')

        task = request.user.tasks.get(id=task_id)
        task.delete()
        return redirect('tasks')

