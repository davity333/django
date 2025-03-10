from django.contrib import admin
from django.urls import path
from tutorial.view import AboutPageView, ReceiveWebSocket,Proyect, Experience, principal, UsersView, Aliado, UserView, ServicesView, ServicesForm, ProyectoForm, ExperienciaForm, AliadoForm
from django.contrib.auth import views as auth_views
from tutorial.viewLogin import LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal.as_view(), name=''),
    path('userForm/', UserView.as_view(), name= 'form_login'),
    path('about', AboutPageView.as_view(), name= 'about'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'), name= 'logout'),
    path('proyect/', Proyect.as_view(), name= 'proyect'),
    path('experiencia/', Experience.as_view(), name= 'experiencia'),
    path('user/', UserView.as_view(), name= 'user'),
    path('aliados/', Aliado.as_view(), name= 'aliados'),
    path('aliadosForm/<int:pk>', AliadoForm.as_view(), name= 'aliadosForm_detail'),
    path('aliadosForm/', AliadoForm.as_view(), name= 'aliadosForm'),
    path('users/', UsersView.as_view(), name='users'),
    path('users/<int:pk>/', UsersView.as_view(), name='user_detail'), 
    path('servicesForm/', ServicesForm.as_view(), name='servicesForm'),
    path('servicesView/', ServicesView.as_view(), name='servicesView'),
    path('servicesView/<int:pk>', ServicesView.as_view(),name = 'servicesView_detail'),
    path('proyectForm/', ProyectoForm.as_view(), name= 'proyectoForm'),
    path('proyectForm/<int:pk>', ProyectoForm.as_view(), name= 'proyectoForm_detail'),
    path('experienceForm/', ExperienciaForm.as_view(), name='experience'),
    path('experienceForm/<int:pk>/', ExperienciaForm.as_view(), name='experience_detail'),
    path('receiveWebSocket',ReceiveWebSocket.as_view(), name='receiveWeSocket'),

]

