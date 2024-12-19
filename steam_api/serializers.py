from rest_framework import serializers
from .models import ExternalData, PlayerPop


class ExternalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalData
        fields = '__all__'

class PlayerPopSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPop
        fields = '__all__'