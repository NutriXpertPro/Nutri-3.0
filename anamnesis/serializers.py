from rest_framework import serializers
from .models import Anamnesis


class AnamnesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anamnesis
        fields = "__all__"
