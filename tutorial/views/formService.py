from django import forms
from tutorial.models.service import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'date', 'description', 'technologies', 'allie']
