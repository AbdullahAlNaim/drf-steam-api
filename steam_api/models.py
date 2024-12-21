from django.db import models
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from django.utils import timezone

load_dotenv()

class ExternalDataManager(models.Manager):
    def fetch_and_save_data(self):
        url = os.environ.get('EXTERNAL_API_URL_1') 
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # data['applist']['apps'][440]['appid']
            # for game in data['applist']['apps']:
            for n in range(10):
                external_data = ExternalData(
                    # game_id = game['appid'],
                    # game_name = game['name']
                    game_id = data['applist']['apps'][n]['appid'],
                    game_name = data['applist']['apps'][n]['name']
                )
                print(f'added {external_data}')
                external_data.save()


# Create your models here.
class ExternalData(models.Model):
    game_id = models.IntegerField()
    game_name = models.CharField(max_length=200)
    # player_pop = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ExternalDataManager()

class SecondExternalDataManager(models.Manager):
    def fetch_and_save_data(self):
        queryset = ExternalData.objects.all()
        for n in range(10):
            steam_game_id = queryset[n].game_id
            url = str(os.environ.get('EXTERNAL_API_URL_2')) + str(steam_game_id)
            response = requests.get(url)
            data = response.json()
            try:
                pop = data['response']['player_count']
                external_data = PlayerCount(
                    game_id = queryset[n].game_id,
                    player_count = pop
                )
                external_data.save()

                print(n, 'adding: ',  steam_game_id,  data['response']['player_count'])
            except KeyError:
                external_data = PlayerCount(
                    game_id = steam_game_id,
                    player_count = 0
                )
                external_data.save()

                print(n, 'adding: ',  data['response']['result'],  0)
        # {"response":{"player_count":40356,"result":1}}

class PlayerPop(models.Model):
    game_id = models.IntegerField()
    player_count = models.IntegerField()
    results = models.IntegerField()

    objects = SecondExternalDataManager()

class PlayerCount(models.Model):
    game_id = models.IntegerField()
    player_count = models.IntegerField()
    # results = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SecondExternalDataManager()
