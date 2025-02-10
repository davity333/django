from django import forms
from tutorial.models.allie import Allies

class AlliesForm(forms.ModelForm):
    class Meta:
        model = Allies
        fields = ['number_colaborator', 'first_colaborator', 'description', 'name_allie']
