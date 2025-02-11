from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .views.formUser import UserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .views.formUser import UserForm
from .views.formProyecto import ProyectForm
from .views.formExperience import ExperienceForm
from .models import OnlyUser
from django.http import JsonResponse
def index(request):
    return HttpResponse("Hello, World!")

class Proyect(TemplateView):
    template_name = 'proyect.html'
    def get(self, request):
        form_instance = ProyectForm()
        return render(request, self.template_name, {'form': form_instance})

    def post(self, request):
        form_instance = ProyectForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('principal')  
        return render(request, self.template_name, {'form': form_instance})

class Experience(TemplateView):
    template_name = 'experience.html'

    def get(self, request):
        form_instance = ExperienceForm()
        return render(request, self.template_name, {'form': form_instance})

    def post(self, request):
        form_instance = ExperienceForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('principal')  
        return render(request, self.template_name, {'form': form_instance})

class User(TemplateView):
    template_name = 'user.html'

class principal(TemplateView):
    template_name = 'principal.html'

  
class formLogin(TemplateView):  
    template_name = 'userForm.html'

class AliadoForm(TemplateView):
    template_name = 'aliados.html'

class UsersView(TemplateView):
    template_name = 'users.html'

class ServicesView(TemplateView):
    template_name ='servicesView.html'

class ServicesForm(TemplateView):
    template_name ='servicesForm.html'

class AliadoForm(TemplateView):
    template_name = 'aliadosUpdate.html'

    def get(self, request):
        form_instance = UserForm()
        return render(request, self.template_name, {'form': form_instance})

    def post(self, request):
        form_instance = UserForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('principal')  
        return render(request, self.template_name, {'form': form_instance})

 
