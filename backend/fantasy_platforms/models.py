from django.db import models

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=255)
    api_url = models.CharField(max_length=255)
