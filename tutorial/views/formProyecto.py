from django import forms
from tutorial.models.proyect import Proyect

class ProyectForm(forms.ModelForm):
    class Meta:
        model = Proyect
        fields = ['name', 'date', 'description', 'technologies', 'allie']
