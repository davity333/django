from django.contrib import admin
from django.urls import path
from tutorial.view import index
from tutorial.view import AboutPageView, Proyect, Experience, principal, UsersView, Aliado, UserView, ServicesView, ServicesForm, ProyectoForm, ExperienciaForm
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal.as_view(), name='principal'),
    path('userForm/', UserView.as_view(), name= 'form_login'),
    path('about', AboutPageView.as_view(), name= 'about'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'), name= 'logout'),
    path('proyect/', Proyect.as_view(), name= 'proyecto'),
    path('experiencia/', Experience.as_view(), name= 'experiencia'),
    path('user/', UserView.as_view(), name= 'user'),
    path('aliados', Aliado.as_view(), name= 'aliados'),
    path('users/', UsersView.as_view(), name='users'),
    path('servicesForm/', ServicesForm.as_view(), name='servicesForm'),
    
    path('servicesView/', ServicesView.as_view(), name='servicesView'),
    path('proyectForm/', ProyectoForm.as_view(), name= 'proyecto'),
    path('experienceForm/', ExperienciaForm.as_view(), name= 'experience'),
]

