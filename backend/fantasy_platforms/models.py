from django.db import models
from authentication.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField(unique= True)
    password = models.CharField(max_length = 100)
    
class Platform(models.Model):
    name = models.CharField(max_length = 150)    

class PlatformToken(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    platform = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name