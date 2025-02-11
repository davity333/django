from django.contrib import admin
from .models import Allies
from .models import Experience
from .models import Service
from .models import OnlyUser
from .models import Proyect

@admin.register(Allies)
class AlliesAdmin(admin.ModelAdmin):
    list_display = ('number_colaborator', 'first_colaborator', 'description', 'name_allie')
@admin.register(Service)    
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'technologies', 'description' ) 
@admin.register(Experience)       
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('description', 'date', 'duration', 'emprise', 'proyect_id')
@admin.register(OnlyUser)
class OnlyUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')
@admin.register(Proyect)
class ProyectAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'description', 'technologies', 'allie')