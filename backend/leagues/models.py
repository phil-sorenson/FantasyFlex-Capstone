from django.db import models
from authentication.models import User
from fantasy_platforms.models import Platform
class League(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, max_length=255)
    league_name = models.CharField(max_length=255)
    league_id = models.CharField(max_length=255, unique=True)
    year = models.CharField(max_length=10)
    
    


    def __str__(self):
        return self.league_name