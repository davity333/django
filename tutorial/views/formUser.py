from django import forms
from tutorial.models.user import OnlyUser  # Asegúrate de que el modelo sea correcto

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=100)

    class Meta:
        model = OnlyUser
        fields = ['name', 'password', 'email'] 