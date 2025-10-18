from django.db import models
from django.conf import settings

# Create your models here.


class Notification(models.Model):
    TYPE_CHOICES = [
        ("EMAIL", "E-mail"),
        ("SMS", "SMS"),
        ("APP", "In-App"),  # Notificação dentro do próprio sistema
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications"
    )
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(
        default=False
    )  # Campo para marcar notificação como lida

    class Meta:
        ordering = ["-sent_at"]

    def __str__(self):
        return f"Notificação para {self.user.name}: {self.message[:30]}..."
