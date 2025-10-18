from django.db import models
from django.conf import settings
from patients.models import Patient

# Create your models here.


class Payment(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pendente"),
        ("PAID", "Pago"),
        ("CANCELLED", "Cancelado"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payments"
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="payments",
    )
    asaas_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        # Garante que o nome do paciente seja exibido, se houver um.
        patient_name = self.patient.name if self.patient else "N/A"
        return f"Pagamento {self.id} - {patient_name}"
