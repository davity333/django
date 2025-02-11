from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect, get_object_or_404
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
from .views.formService import ServiceForm
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from .models import Service

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

class ServicesView(TemplateView):
    template_name ='servicesView.html'

class ServicesForm(TemplateView):
    template_name ='servicesForm.html'

class AliadoForm(TemplateView):
    template_name = 'aliadosUpdate.html'

class ProyectoForm(TemplateView):
    template_name = 'proyectForm.html'

class ExperienciaForm(TemplateView):
    template_name = 'ExperienceForm.html'

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
class Aliado(TemplateView):
    template_name = 'aliados.html'
class BasePageView(TemplateView):
    template_name = 'base.html'    
class UserView(TemplateView):
    template_name = 'userForm.html'

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')  # Redirigir a la lista de usuarios después del registro
        return self.render_to_response({'form': form})
class UsersView(TemplateView):
    template_name = 'users.html'

    def get(self, request, pk=None):
      """Obtiene y muestra la lista de usuarios o un usuario específico si se proporciona pk."""
      if pk:
        user = get_object_or_404(OnlyUser, pk=pk)
        return render(request, self.template_name, {'user': user, 'edit': True})
      users = OnlyUser.objects.all()
      return render(request, self.template_name, {'users': users, 'edit': False})

    def put(self, request, pk):
        """Edita un usuario existente."""
        try:
            user = OnlyUser.objects.get(pk=pk)
            form = UserForm(request.PUT, instance=user)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Usuario actualizado'}, status=200)
            return JsonResponse({'error': 'Formulario no válido'}, status=400)
        except OnlyUser.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

    def post(self, request, pk=None):
        user_id = request.POST.get('user_id')  
        if user_id:
            try:
                user = OnlyUser.objects.get(id=user_id)
                user.delete()  
                return redirect('users')  
            except OnlyUser.DoesNotExist:
                pass  
        if pk:
            # Editar usuario
            user = get_object_or_404(OnlyUser, pk=pk)
            user.name = request.POST.get('name')
            user.email = request.POST.get('email')
            user.password = request.POST.get('password')  # Asegúrate de manejar la contraseña de forma segura
            user.save()
            return redirect('users')
        return redirect('users')

#SERVICES
class ServiceListView(TemplateView):
    template_name = 'servicesView.html'

    def get(self, request):
        services = Service.objects.all()
        return render(request, self.template_name, {'services': services})

class ServiceCreateView(View):
    template_name = 'serviceForm.html'

    def get(self, request):
        form = ServiceForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicesView')
        return render(request, self.template_name, {'form': form})

class ServiceUpdateView(View):
    template_name = 'serviceForm.html'

    def get(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        form = ServiceForm(instance=service)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('servicesView')
        return render(request, self.template_name, {'form': form})

class ServiceCreateView(View):
    template_name = 'serviceForm.html'

    def get(self, request):
        form = ServiceForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicesView')  # Redirige después de guardar
        return render(request, self.template_name, {'form': form})
