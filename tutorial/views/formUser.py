# formUser.py
from django import forms
from tutorial.models.user import OnlyUser

class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True) 

    class Meta:
        model = OnlyUser
        fields = ['name', 'password', 'email']