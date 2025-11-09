from django.db import models
from django.utils import formats
from patients.models import PatientProfile

# Create your models here.


class Evaluation(models.Model):
    METHOD_CHOICES = [
        ('ADIPOMETRO', 'Adipômetro'),
        ('BIOIMPEDANCIA', 'Bioimpedância'),
        ('FITA_METRICA', 'Fita Métrica (Método da Marinha)'),
    ]

    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, related_name="evaluations", null=True
    )
    date = models.DateTimeField()
    
    # New fields
    method = models.CharField(
        max_length=20,
        choices=METHOD_CHOICES,
        null=True,
        blank=True,
        db_index=True # Added for performance
    )
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Altura em metros (ex: 1.75)")
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Peso em kg (ex: 70.5)")
    body_fat = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, help_text="Percentual de gordura (ex: 22.5)")
    muscle_mass = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Massa muscular em kg (ex: 55.2)")

    body_measurements = models.JSONField(null=True, blank=True, help_text="Medidas corporais em JSON (circunferências, dobras cutâneas, etc.)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordena as avaliações da mais recente para a mais antiga por padrão
        ordering = ["-date"]

    def __str__(self):
        date_str = formats.date_format(self.date, "d/m/Y")
        return f"Avaliação de {self.patient.user.name} em {date_str}"


class EvaluationPhoto(models.Model):
    LABEL_CHOICES = [
        ('FRENTE', 'Frente'),
        ('LADO', 'Lado'),
        ('COSTAS', 'Costas'),
    ]
    evaluation = models.ForeignKey(Evaluation, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='evaluation_photos/%Y/%m/%d/')
    label = models.CharField(max_length=10, choices=LABEL_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto de {self.evaluation.patient.user.name} - {self.get_label_display()}"