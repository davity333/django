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

def index(request):
    return HttpResponse("Hello, World!")

class Proyect(TemplateView):
    template_name = 'proyect.html'

class Aliado(TemplateView):
    template_name = 'aliados.html'

class Experience(TemplateView):
    template_name = 'experience.html'

class User(TemplateView):
    template_name = 'user.html'

class principal(TemplateView):
    template_name = 'principal.html'

class formLogin(TemplateView):  
    template_name = 'userForm.html'

class AliadoForm(TemplateView):
    template_name = 'aliados.html'

    def get(self, request):
        form_instance = UserForm()
        return render(request, self.template_name, {'form': form_instance})


class users(TemplateView):
    template_name = 'users.html'



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

 
