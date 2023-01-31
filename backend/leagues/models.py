from django.db import models
from authentication.models import User
# from fantasy_platforms.models import Platform
# Create your models here.

class League(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=255)
    league_name = models.CharField(max_length=255)
    league_id = models.IntegerField(max_length=255, unique=True)
    # is_imported tracks whether league was imported to user's account or not
    is_imported = models.BooleanField(default=False)

    def __str__(self):
        return self.league_name