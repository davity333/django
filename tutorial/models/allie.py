from django.db import models

class Allies(models.Model):
    number_colaborator = models.IntegerField()
    first_colaborator = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    name_allie = models.CharField(max_length=100)
    def __str__(self):
        return self.name_allie