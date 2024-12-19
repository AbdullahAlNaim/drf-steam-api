from django.shortcuts import render
from .models import ExternalData, PlayerPop
from .serializers import ExternalDataSerializer, PlayerPopSerializer
from rest_framework import generics
import requests
from dotenv import load_dotenv

# Create your views here.
class SteamGames(generics.ListAPIView):
    queryset = ExternalData.objects.all()
    serializer_class = ExternalDataSerializer

# {
#     "id": 3511,
#     "game_id": 2144380,
#     "game_name": "The Apocalypse Playtest",
#     "created_at": "2024-12-19T02:57:49.367756Z",
#     "updated_at": "2024-12-19T02:57:49.367840Z"
# },
# {"appid":3342090,"name":"Second Works"}


class PlayerCount(generics.ListAPIView):
    # queryset = PlayerPop.objects.all()
    # serializer_class = PlayerPopSerializer
    def get(self, request):
        try:
            url = os.environ.get('EXTERNAL_API_URL_2')
        except Exception as e:
            return Response()




# class MyAPIView(APIView):
#     def get(self, request):
#         external_data_url = "https://api.example.com/data"
#         data = fetch_external_data(external_data_url)
#         processed_data = process_external_data(data)
#         return Response(processed_data)