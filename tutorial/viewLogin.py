from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .models import OnlyUser  # Asegúrate de usar el modelo correcto

class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Verifica si los campos están vacíos
        if not email or not password:
            return render(request, self.template_name, {"error": "Por favor, completa todos los campos"})

        try:
            user = OnlyUser.objects.get(email=email)  # Busca el usuario en la tabla `users`
        except OnlyUser.DoesNotExist:
            return render(request, self.template_name, {"error": "Usuario no encontrado"})

        if user.check_password(password):  # Verifica la contraseña
            login(request, user)
            return redirect('principal')  # Cambia "principal" por la URL que prefieras
        else:
            return render(request, self.template_name, {"error": "Contraseña incorrecta"})