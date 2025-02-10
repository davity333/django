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

    def get(self, request):
        form_instance = UserForm()
        return render(request, self.template_name, {'form': form_instance})

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
            return redirect('')
        return self.render_to_response({'form': form})
class UsersView(TemplateView):
    template_name = 'users.html'

    def get(self, request):
        """Obtiene y muestra la lista de usuarios."""
        users = OnlyUser.objects.all()
        return render(request, self.template_name, {'users': users})
    def put(self, request, pk):
        """Edita un usuario existente."""
        try:
            user = OnlyUser.objects.get(pk=pk)
            form = UserForm(request.PUT, instance=user)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Usuario actualizado'}, status=200)
            return JsonResponse({'error': 'Formulario no válido'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

    def delete(self, request, pk):
        """Elimina un usuario."""
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return JsonResponse({'message': 'Usuario eliminado'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
