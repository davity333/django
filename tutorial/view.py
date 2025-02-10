from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .views.formUser import UserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from .views.formUser import UserForm
from .views.formProyecto import ProyectForm

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

class User(TemplateView):
    template_name = 'user.html'


class principal(TemplateView):
    template_name = 'principal.html'

  
class formLogin(TemplateView):  
    template_name = 'userForm.html'

    def get(self, request):
        form_instance = UserForm()
        return render(request, self.template_name, {'form': form_instance})


class users(TemplateView):
    template_name = 'users.html'


class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Carrera
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["saludo"] = "Hola de nuevo"
        context["lista"] = Carrera.objects.all()    
        return context

#direccionar a otra


    @method_decorator(login_required, name='dispatch')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    

    def post(self, request):
        form_instance = UserForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('principal')  
        return render(request, self.template_name, {'form': form_instance})

class AboutPageView(TemplateView):
    template_name = 'about.html'
class BasePageView(TemplateView):
    template_name = 'base.html'    
from django.views.generic import TemplateView
from .views.formUser import UserForm

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .views.formUser import UserForm

class UserView(TemplateView):
    template_name = 'user.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
        context = {'form': form}
        return self.render_to_response(context)    

def agregar_usuario(request):
    return render(request, 'userForm.html') 
            return redirect('')
        return self.render_to_response({'form': form})
