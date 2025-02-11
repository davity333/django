from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
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

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"  # Usar email en lugar de username
    REQUIRED_FIELDS = ["nombre"]  # Asegúrate de que 'nombre' es un campo obligatorio

    def __str__(self):
        return self.email
class OnlyUser( AbstractBaseUser, PermissionsMixin, models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'  # Aquí indicamos que el email es el campo principal
    REQUIRED_FIELDS = ['name'] 
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='onlyuser_set',  # Evitar el conflicto con auth.User
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='onlyuser_set',  # Evitar el conflicto con auth.User
        blank=True
    )

    def __str__(self):
        return self.name
