from django.db import models
from django.conf import settings
from patients.models import PatientProfile

# Create your models here.


class Appointment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="appointments"
    )
    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, related_name="appointments"
    )
    date = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        date_str = self.date.strftime("%d/%m/%Y %H:%M")
        return f"Agendamento de {self.patient.user.name} em {date_str}"
