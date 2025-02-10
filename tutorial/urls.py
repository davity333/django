"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from tutorial.view import index
from tutorial.view import HomePageView,AboutPageView,BasePageView,CarrerasCreateView, Proyect, Experience, User, principal, formLogin
from django.contrib.auth import views as auth_views
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

]
