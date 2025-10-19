from django.db import models
from patients.models import Patient

# Create your models here.


class Diet(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="diets")
    name = models.CharField(max_length=255)
    meals = models.JSONField()
    substitutions = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def add_substitution(self, substitution_data):
        if not isinstance(self.substitutions, dict):
            self.substitutions = {}
        self.substitutions.update(substitution_data)
        self.save()

    def add_meal(self, meal_data):
        if not isinstance(self.meals, list):
            self.meals = []
        self.meals.append(meal_data)
        self.save()

    def __str__(self):
        return f"{self.name} - {self.patient.name}"
