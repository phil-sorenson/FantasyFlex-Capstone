from rest_framework import serializers
from .models import League


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'user' 'platform', 'league_name', 'league_id']
        #?❓Would 'platform' need to be in here since the platform will already be chosen by user once he is told to pick through his leagues and we have a fantasy_platforms app already

class GetLeaguesSerializer(serializers.Serializer):
#  This serializer class will validate the data coming in from the user's selected leagues API call
    platform_id = serializers.IntegerField()
    selected_leagues = serializers.ListField(child = serializers.IntegerField())