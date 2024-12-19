from django.urls import path
from . import views

urlpatterns = [
    path('', views.SteamGames.as_view(), name='steam-games')
]