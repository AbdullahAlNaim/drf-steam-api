from django.shortcuts import render
from .models import ExternalData, PlayerCount
from .serializers import ExternalDataSerializer, PlayerPopSerializer
from rest_framework import generics
import os
from dotenv import load_dotenv

load_dotenv()

# Create your views here.
class SteamGames(generics.ListAPIView):
    queryset = ExternalData.objects.all()
    serializer_class = ExternalDataSerializer


class PlayerCount(generics.ListAPIView):
    queryset = PlayerCount.objects.all()
    serializer_class = PlayerPopSerializer

