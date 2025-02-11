from django.contrib import admin
from django.urls import path
from tutorial.view import index
from tutorial.view import Proyect, Experience, User, principal, formLogin, UsersView, AliadoForm, ServicesForm, ServicesView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal.as_view(), name='principal'),  # Esta será la vista por defecto
    path('userForm/', formLogin.as_view(), name='form_login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('proyect/', Proyect.as_view(), name='proyecto'),
    path('experiencia/', Experience.as_view(), name='experiencia'),
    path('user/', User.as_view(), name='user'),
    path('users/', UsersView.as_view(), name='users'),
    path('aliados/', AliadoForm.as_view(), name='aliados'),
    path('servicesForm/', ServicesForm.as_view(), name='servicesForm'),
    path('servicesView/', ServicesView.as_view(), name='servicesView')

]

