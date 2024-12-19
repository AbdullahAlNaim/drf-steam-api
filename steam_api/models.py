from django.db import models
import requests
import os
from dotenv import load_dotenv

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

class SecondExternalDataManager(models.Manager):
    def fetch_and_save_data(self):
        url = os.environ.get('EXTERNAL_API_URL_2') 
        # {"response":{"player_count":40356,"result":1}}

# Create your models here.
class ExternalData(models.Model):
    game_id = models.IntegerField()
    game_name = models.CharField(max_length=200)
    # player_pop = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ExternalDataManager()

class PlayerPop(models.Model):
    game_id = models.IntegerField()
    player_count = models.IntegerField()
    results = models.IntegerField()





