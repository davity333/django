from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UsesManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class Uses(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsesManager()

    USERNAME_FIELD = "email"  # Usar email en lugar de username
    REQUIRED_FIELDS = ["nombre"]  # Asegúrate de que 'nombre' es un campo obligatorio

    def __str__(self):
        return self.email
