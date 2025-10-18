from django.db import models
from django.conf import settings

# Create your models here.


class Patient(models.Model):
    # Link para o nutricionista (o usuário logado)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patients"
    )

    # Campos de dados do paciente
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Isso faz com que o nome do paciente apareça na listagem do admin
    def __str__(self):
        return self.name
