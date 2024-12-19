from django.shortcuts import render
from .models import ExternalData, PlayerPop
from .serializers import ExternalDataSerializer, PlayerPopSerializer
from rest_framework import generics

# Create your views here.
class SteamGames(generics.ListAPIView):
    queryset = ExternalData.objects.all()
    serializer_class = ExternalDataSerializer

