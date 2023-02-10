from rest_framework import serializers
from .models import SleeperUser


class SleeperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleeperUser
        fields = ['id', 'username', 'user_id',
                  'avatar', 'display_name']
