from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    """Manager customizado para o nosso modelo de User."""

    def create_user(self, email, password=None, **extra_fields):
        """Cria e salva um novo usuário com o email e senha fornecidos."""
        if not email:
            raise ValueError("O email é um campo obrigatório.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Cria e salva um novo superusuário."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Modelo de usuário customizado que usa email como login."""

    USER_TYPE_CHOICES = (
        ("nutricionista", "Nutricionista"),
        ("paciente", "Paciente"),
        ("admin", "Admin"),  # Adicionado para o superusuário
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default="paciente",  # Valor padrão para novos usuários
    )
    is_staff = models.BooleanField(default=False)  # Necessário para acesso ao admin
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"  # Define o campo de login
    REQUIRED_FIELDS = ["name", "user_type"]  # user_type agora é um campo obrigatório

    def __str__(self):
        return self.email
