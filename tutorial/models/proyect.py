from django.db import models
from django.db.models import SET_NULL 
from .allie import Allies
class Proyect(models.Model):
    name = models.CharField(max_length=255)  # Agregar max_length
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=255)  # Puede ser más largo si es necesario
    technologies = models.CharField(max_length=255)
    allie = models.ForeignKey(Allies, on_delete=SET_NULL, null=True, blank=True)  # Corrección

    def __str__(self):
        return self.name