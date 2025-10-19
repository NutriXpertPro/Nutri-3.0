from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna apenas as notificações não lidas para o usuário autenticado
        return Notification.objects.filter(user=self.request.user, is_read=False)


@login_required
def unread_notifications_htmx(request):
    notifications = Notification.objects.filter(
        user=request.user, is_read=False
    ).order_by("-sent_at")[
        :5
    ]  # Get latest 5 unread notifications
    serializer = NotificationSerializer(notifications, many=True)
    return render(
        request,
        "notifications/_unread_notifications.html",
        {"notifications": serializer.data},
    )
