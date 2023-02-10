from django.db import models
# from authentication.models import User


class SleeperUser(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, default='default')
    user_id = models.CharField(max_length=200, default='default')
    display_name = models.CharField(max_length=150, default='default')
    avatar = models.CharField(max_length=150, default='default')
