from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import OnlyUser 

class LoginView(View):
    template_name = "login.html"
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        if not email or not password:
            return render(request, self.template_name, {"error": "Por favor, completa todos los campos"})
        try:
            user = OnlyUser.objects.get(email=email)  
        except OnlyUser.DoesNotExist:
            return render(request, self.template_name, {"error": "Usuario no encontrado"})
        if user.check_password(password):  
            login(request, user)
            return redirect('') 
        else:
            return render(request, self.template_name, {"error": "Contraseña incorrecta"})
def logout_view(request):
    logout(request)
    return redirect('login') 