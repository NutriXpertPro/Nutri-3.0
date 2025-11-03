from django.db import models
from patients.models import PatientProfile

# Create your models here.


class Anamnesis(models.Model):
    # Campo One-to-One: Cada paciente tem uma única anamnese.
    patient = models.OneToOneField(
        PatientProfile, on_delete=models.CASCADE, primary_key=True
    )

    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    medical_conditions = models.JSONField(null=True, blank=True)
    food_preferences = models.JSONField(null=True, blank=True)
    allergies = models.JSONField(null=True, blank=True)
    photo_url = models.URLField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Anamnese de {self.patient.user.name}"
