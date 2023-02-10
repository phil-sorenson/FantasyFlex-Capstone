from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from django.shortcuts import get_object_or_404
from rest_framework import status, permissions, generics
# from sleeper_wrapper import User
# from django.http import JsonResponse
import json
import requests

from .serializers import SleeperUserSerializer
from .models import SleeperUser
# AUTH LOGIN ROUTE -- (POST) - Create a token if credentials match


# GET request 'login' that extracts the 'user_id' upon a 200 status code
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def login(request, username):
    response = requests.get(f'https://api.sleeper.app/v1/user/{username}')
    data = response.json()
    serializer = SleeperUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        # user_id = serializer.validated_data['user_id']
        # avatar = serializer.validated_data['avatar']
        # display_name = serializer.validated_data['display_name']
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def logged_user(request, username):
    if request.method == 'POST':
        # user_id = request.data.get('user_id')
        # avatar = request.data.get('avatar')
        # display_name = request.data.get('display_name')
        user = SleeperUser.objects.create(username=username)
        serializer = SleeperUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# class SleeperUserCreate(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = SleeperUser.objects.all()
#     serializer_class = SleeperUserSerializer
