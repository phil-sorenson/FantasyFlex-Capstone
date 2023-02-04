from django.shortcuts import render
from .models import Platform, League
from .serializers import PlatformSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404



# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_platforms(request):
# # Code to retrieve a list of avb platforms
#     platforms = Platform.objects.all()
#     serializer = PlatformSerializer(platforms, many=True)
#     return Response(serializer.data, status = status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def login_to_platform(request):
# Code to handle user logging in to the selected platform (Just Sleeper for now)
    platform_id = request.data.get('platform_id')
    platform = Platform.objects.get(id=platform_id)
