from django.db import models
from patients.models import PatientProfile

class LabExam(models.Model):
    patient = models.ForeignKey(
        PatientProfile, 
        related_name='lab_exams', 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, verbose_name="Nome do Exame")
    date = models.DateField(verbose_name="Data do Exame")
    attachment = models.FileField(
        upload_to='lab_exams/%Y/%m/%d/', 
        verbose_name="Anexo do Exame"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Exame Laboratorial"
        verbose_name_plural = "Exames Laboratoriais"

    def __str__(self):
        return f"{self.name} - {self.patient.user.name} em {self.date.strftime('%d/%m/%Y')}"