from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect, get_object_or_404
from .views.formUser import UserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .views.formUser import UserForm
from .views.formProyecto import ProyectForm
from .views.formExperience import ExperienceForm
from .models import OnlyUser
from  .views.formAllie import AlliesForm
from .views.formService import ServiceForm
from django.http import JsonResponse
from .views.formService import ServiceForm
import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Proyect as ProyectModel, Experience as ExperienceModel, Allies
from django.contrib.auth.decorators import permission_required

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
            return redirect('')  
        return render(request, self.template_name, {'form': form_instance})

class User(TemplateView):
    template_name = 'user.html'

class principal(TemplateView):
    template_name = 'principal.html'

  
class formLogin(TemplateView):  
    template_name = 'userForm.html'


class ServicesView(TemplateView):
    template_name = 'servicesView.html'

    def get(self, request, pk=None):
        if pk:
            # Si existe pk, obtener el servicio para editar
            service = get_object_or_404(Service, pk=pk)
            return render(request, self.template_name, {'service': service, 'edit': True})
        # Si no existe pk, obtener todos los servicios
        services = Service.objects.all()
        return render(request, self.template_name, {'services': services, 'edit': False})

    def post(self, request, pk=None):
        service_id = request.POST.get('service_id')
        if service_id:
            try:
                service = Service.objects.get(id=service_id)
                service.delete()
                return redirect('servicesView')
            except Service.DoesNotExist:
                pass
        if pk:
            service = get_object_or_404(Service, pk=pk)
            service.name = request.POST.get('name')
            service.description = request.POST.get('description')
            service.technologies = request.POST.get('technologies')
            service.save()
            return redirect('servicesView')

        return redirect('servicesView') 
class ServicesForm(TemplateView):
    template_name ='servicesForm.html'
    def get(self, request, *args, **kwargs):
        form = ServiceForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicesView')
        return self.render_to_response({'form': form})


class AliadoForm(TemplateView):
    template_name = 'aliadosUpdate.html'
    def get(self, request, pk=None):
        if pk:
            aliado = get_object_or_404(Allies, pk=pk)
            form = AlliesForm(instance=aliado)  # Formulario con datos del aliado existente
        else:
            form = AlliesForm()  # Formulario vacío para crear un nuevo aliado

        allies = Allies.objects.all()  # Obtener todos los aliados
        return render(request, self.template_name, {'form': form, 'allies': allies, 'edit': pk is not None})

    def post(self, request, pk=None):
        aliado_id = request.POST.get('aliado_id')

        if aliado_id:
            aliado = Allies.objects.filter(id=aliado_id).first()
            if aliado:
                aliado.delete()
                return redirect('aliadosForm') 
        form = None

        if pk:
            aliado = get_object_or_404(Allies, pk=pk)
            form = AlliesForm(request.POST, instance=aliado)  # Actualizar aliado existente
        if form and form.is_valid():
            form.save()
            return redirect('aliadosForm')

        # Si no se inicializó `form` correctamente, aseguramos que siempre tenga un valor
        if form is None:
            form = AlliesForm()

        allies = Allies.objects.all()
        return render(request, self.template_name, {'form': form, 'allies': allies, 'edit': pk is not None})


class ProyectoForm(TemplateView):
    template_name = 'proyectForm.html'

    def get(self, request, pk=None):
        if pk:
            proyect = get_object_or_404(ProyectModel, pk=pk)
            form = ProyectForm(instance=proyect)
            return render(request, self.template_name, {'form': form, 'edit': True})
        projects = ProyectModel.objects.all()

        return render(request, self.template_name, {'proyects': projects, 'edit': False})

    def post(self, request, pk=None):
     proyect_id = request.POST.get('proyect_id')
     if proyect_id:
        try:
            proyect = ProyectModel.objects.get(id=proyect_id)
            proyect.delete()
            return redirect('proyectoForm')  # Redirige sin pasar 'pk'
        except ProyectModel.DoesNotExist:
            pass

     if pk:
        proyect = get_object_or_404(ProyectModel, pk=pk)
        form = ProyectForm(request.POST, instance=proyect)
        if form.is_valid():
            form.save()
            return redirect('proyectoForm')
     else:

        form = ProyectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyectoForm')

     return render(request, self.template_name, {'form': form, 'edit': True})

class ExperienciaForm(TemplateView):
    template_name = 'experienceForm.html'
    form_class = ExperienceForm

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            # Si hay una pk, obtenemos el objeto Experience para editarlo
            experiencia = get_object_or_404(ExperienceModel, pk=pk)
            form = self.form_class(instance=experiencia)
        else:
            # Si no hay pk, es un formulario de creación
            form = self.form_class()

        # Obtenemos todas las experiencias para pasarlas al template
        experiencias = ExperienceModel.objects.all()

        return self.render_to_response({
            'form': form,
            'experiencias': experiencias  # Pasamos las experiencias al template
        })

    def post(self, request, pk=None, *args, **kwargs):
        
        if pk:
            experiencia = get_object_or_404(ExperienceModel, pk=pk)
            form = self.form_class(request.POST, instance=experiencia)
        else:
            form = self.form_class(request.POST)
        experience_id = request.POST.get('experience_id')  
        if experience_id:
            try:
                user = ExperienceModel.objects.get(id=experience_id)
                user.delete()  
                return redirect('experience')  
            except ExperienceModel.DoesNotExist:
                pass  
        if form.is_valid():
            form.save()
            return redirect('experience')  
        experiencias = ExperienceModel.objects.all()
        return self.render_to_response({
            'form': form,
            'experiencias': experiencias  
        })
class AboutPageView(TemplateView):
    template_name = 'about.html'  
@method_decorator(permission_required('tutorial.add_allie', login_url='aliadosForm', raise_exception=False), name='dispatch')    
class Aliado(TemplateView):
    template_name = 'aliados.html'

    def get(self, request):
        # Mostrar el formulario vacío
        form = AlliesForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Procesar el formulario cuando se envía
        form = AlliesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')  # Redirigir a la misma página o a una página de éxito
        return render(request, self.template_name, {'form': form})

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
            user = form.save(commit=False)  # No guarda inmediatamente el usuario
            user.set_password(form.cleaned_data['password'])  # Hashea la contraseña
            user.save()  # Ahora sí guarda el usuario con la contraseña hasheada
            return redirect('users')  # Redirige a la lista de usuarios después del registro
        return self.render_to_response({'form': form})
class UsersView(TemplateView):
    template_name = 'users.html'

    def get(self, request, pk=None):
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
            user.password = request.POST.get('password')  
            user.save()
            return redirect('users')
        return redirect('users')

#SERVICES
class ServiceListView(TemplateView):
    template_name = 'servicesView.html'

    def get(self, request):
        services = Service.objects.all()
        return render(request, self.template_name, {'services': services})

class ServiceUpdateView(TemplateView):
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

class ServiceCreateView(TemplateView):
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
