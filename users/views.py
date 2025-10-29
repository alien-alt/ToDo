from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import User
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        else:
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

class DetailTasksView(TemplateView):
    template_name = 'task_detail.html'

class CompletedTasksView(TemplateView):
    template_name = 'completed_tasks.html'

class AddTaskView(TemplateView):
    template_name = 'add_task.html'

"""POST views"""
class MakeRegisterView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST

        username = data['username']
        password = data['password']

        is_fields_not_empty =  username != "" and password != ""
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

        username = data['username']
        password = data['password']

        is_fields_not_empty =  username != "" and password != ""

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
