from django.db import models


# platform_id
class Platform(models.Model):
    SLEEPER = 'Sleeper'
    YAHOO = 'Yahoo'
    PLATFORM_CHOICES = [
        (SLEEPER, 'Sleeper'),
        (YAHOO, 'Yahoo'),
    ]
    name = models.CharField(
        max_length=100,
        choices = PLATFORM_CHOICES,
        default= SLEEPER
    )

    def __str__(self):
        return self.name