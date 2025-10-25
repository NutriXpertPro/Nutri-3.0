from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna conversas onde o usuário logado é um participante
        return Conversation.objects.filter(participants=self.request.user).order_by(
            "-updated_at"
        )

    def perform_create(self, serializer):
        # Garante que o usuário logado seja um participante da conversa
        conversation = serializer.save()
        conversation.participants.add(self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna mensagens de conversas onde o usuário logado é um participante
        conversation_id = self.kwargs["conversation_pk"]  # Obtido da URL aninhada
        return Message.objects.filter(
            conversation__id=conversation_id,
            conversation__participants=self.request.user,
        ).order_by("timestamp")

    def perform_create(self, serializer):
        # Garante que o remetente da mensagem seja o usuário logado
        conversation_id = self.kwargs["conversation_pk"]
        conversation = Conversation.objects.get(id=conversation_id)
        serializer.save(sender=self.request.user, conversation=conversation)

    @action(detail=True, methods=["post"])
    def mark_as_read(self, request, pk=None, conversation_pk=None):
        message = self.get_object()
        if message.conversation.participants.filter(id=request.user.id).exists():
            message.is_read = True
            message.save()
            return Response({"status": "message marked as read"})
        return Response(
            {"detail": "Not authorized to mark this message as read"},
            status=status.HTTP_403_FORBIDDEN,
        )


@login_required
def inbox_view(request):
    return render(request, "messages/inbox.html", {})
