from django.db import models
from django.db.models import SET_NULL 
from .proyect import Proyect
class Experience(models.Model):
    description = models.IntegerField()
    date = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    emprise = models.CharField(max_length=100)
    proyect_id = models.ForeignKey(Proyect, on_delete = SET_NULL, null=True)
    def __str__(self):
        return self.description