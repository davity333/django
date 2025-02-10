from django.db import models
from .allie import Allies
class Service(models.Model):
    name = models.CharField(max_length=100)
    technologies = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name