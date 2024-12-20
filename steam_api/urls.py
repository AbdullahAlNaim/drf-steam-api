from django.urls import path
from . import views

urlpatterns = [
    path('', views.SteamGames.as_view(), name='steam-games'),
    path('players/', views.PlayerCount.as_view(), name='player-counts')
]