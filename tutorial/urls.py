from django.contrib import admin
from django.urls import path
from tutorial.view import index
from tutorial.view import HomePageView,AboutPageView,BasePageView,CarrerasCreateView, Proyect, Experience, User, principal, formLogin, users
from django.contrib.auth import views as auth_views
from tutorial import view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', principal.as_view(), name='principal'),
    path('userForm/', formLogin.as_view(), name= 'form_login'),
    path('', HomePageView.as_view(), name= 'home'),
    path('about', AboutPageView.as_view(), name= 'about'),
    path('carrera/crear',CarrerasCreateView.as_view(), name= 'carrera_crear'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'), name= 'logout'),
    path('proyect/', Proyect.as_view(), name= 'proyecto'),
    path('experiencia/', Experience.as_view(), name= 'experiencia'),
    path('user/', User.as_view(), name= 'user'),
    path('users/', users.as_view(), name= 'users'),
]
from django.urls import path, include
from tutorial.view import index, AboutPageView, BasePageView, Proyect, Experience, UserView, principal, formLogin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Cambiar esto # Usar la ruta raíz para tutorial.urls
    path('principal/', principal.as_view(), name='principal'),
    path('userForm/', formLogin.as_view(), name='form_login'),
    path('about/', AboutPageView.as_view(), name='about'),  # Asegúrate de agregar la barra '/'
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('proyect/', Proyect.as_view(), name='proyecto'),
    path('experiencia/', Experience.as_view(), name='experiencia'),
    path('user/', UserView.as_view(), name='user'),
]
