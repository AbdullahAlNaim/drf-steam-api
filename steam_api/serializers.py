from rest_framework import serializers
from .models import ExternalData, PlayerCount


class ExternalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalData
        fields = '__all__'

class PlayerPopSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerCount
        fields = '__all__'