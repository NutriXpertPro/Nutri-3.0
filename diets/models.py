from django.db import models
from patients.models import Patient

# Create your models here.


class Diet(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="diets")
    name = models.CharField(max_length=255)
    meals = models.JSONField()
    substitutions = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.patient.name}"
