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
# Takes in the Sleeper API endpoint (user info via username)-- returns as JSON and saves data if valid
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def login(request, username):
    if request.method == 'GET':
        response = requests.get(f'https://api.sleeper.app/v1/user/{username}')
        user_data = response.json()
        try:
            user = SleeperUser.objects.get(username=username)
            serializer = SleeperUserSerializer(
                user, data=user_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
        except SleeperUser.DoesNotExist:
            serializer = SleeperUserSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SleeperUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Todo: Create a delete leagues function
