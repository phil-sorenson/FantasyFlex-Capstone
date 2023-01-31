# from django.shortcuts import render
from .models import League
from .serializers import LeagueSerializer
from rest_framework import viewsets
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from django.shortcuts import get_object_or_404

# Todo: Create a view function that filter's the selected leagues and GETS all the league ID's  

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_leagues(request):
# # We want this code to just return the list of ALL leagues once user log-ins to platform (GET league with username or user_id)-- Frontend??
#     leagues = League.objects.filter(user = request.user)
#     serializer = LeagueSerializer(leagues, many=True)
#     return Response(serializer.data, status = status.HTTP_200_OK)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def import_leagues(request):
# # Import the user's selected leagues to Fantasy Flex application (GET league w/ league_id) --  
#     selected_leagues = request.data.get

class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer