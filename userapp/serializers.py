from rest_framework import serializers
from .models import UserProfile  # Substitua pelo nome correto do modelo

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'  # Pode ajustar os campos conforme necessário
