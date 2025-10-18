from django.db import models
from django.utils import formats
from patients.models import Patient

# Create your models here.


class Evaluation(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="evaluations"
    )
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    body_measurements = models.JSONField(null=True, blank=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordena as avaliações da mais recente para a mais antiga por padrão
        ordering = ["-date"]

    def __str__(self):
        date_str = formats.date_format(self.date, "d/m/Y")
        return f"Avaliação de {self.patient.name} em {date_str}"
