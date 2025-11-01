from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.


class Patient(models.Model):  # Renomear para PatientProfile no futuro
    # Link para o usuário do paciente (One-to-One)
    patient_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patient_profile",
        null=True,
    )

    # Link para o nutricionista responsável
    nutritionist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="managed_patients",
        limit_choices_to={"user_type": "nutricionista"},
        null=True,
    )

    # Campos de dados do paciente (email e name podem ser removidos se já
    # estiverem no User)
    # name = models.CharField(max_length=255) # Já está no User
    # email = models.EmailField(max_length=255, null=True, blank=True) # Já está no User
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_age(self):
        if self.birth_date:
            today = date.today()
            return (
                today.year
                - self.birth_date.year
                - (
                    (today.month, today.day)
                    < (self.birth_date.month, self.birth_date.day)
                )
            )
        return None

    def __str__(self):
        return self.patient_user.name  # Retorna o nome do usuário paciente
