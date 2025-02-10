from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .models import Uses  # Asegúrate de usar el modelo correcto

class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Uses.objects.get(email=email)  # Busca el usuario en la tabla `uses`
        except Uses.DoesNotExist:
            user = None

        if user and user.check_password(password):  # Verifica la contraseña
            login(request, user)
            return redirect("home")  # Cambia "home" por la URL que prefieras
        else:
            return render(request, self.template_name, {"error": "Usuario o contraseña incorrectos"})
