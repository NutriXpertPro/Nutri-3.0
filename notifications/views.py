from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer


from rest_framework.decorators import action
from rest_framework.response import Response


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the unread notifications
        for the currently authenticated user.
        """
        return Notification.objects.filter(
            user=self.request.user, is_read=False
        ).order_by("-sent_at")

    @action(detail=False, methods=["post"])
    def mark_all_as_read(self, request):
        """Marks all unread notifications for the user as read."""
        unread_notifications = self.get_queryset().filter(is_read=False)
        unread_notifications.update(is_read=True)
        return Response({"status": "all notifications marked as read"})


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
