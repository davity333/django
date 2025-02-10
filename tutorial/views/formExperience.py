from django import forms
from tutorial.models.experience import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['description', 'date', 'description', 'duration', 'emprise', 'proyect_id']
        