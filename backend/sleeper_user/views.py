
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from sleeper_wrapper import User
from django.http import JsonResponse
import json
import requests

from .serializers import SleeperUserSerializer
from .models import SleeperUser
# AUTH LOGIN ROUTE -- (POST) - Create a token if credentials match ('/sleeperlogin')


# GET request 'login' that extracts the 'user_id' upon a 200 status code
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def login(request):
    username = request.data.get('username')
    response = requests.get(f'https://api.sleeper.app/v1/user/{username}')
    if response.status_code == 200:
        # user_id = response.json().get('user_id')
        # Extracts the 'user_id' from the GET username request JSON response
        SleeperUser.objects.create(username=username)
        # Saves the username to the sleeperUser model
        return Response({'message': 'Login Successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Login Failed'}, status=status.HTTP_400_BAD_REQUEST)


# @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def login_user(request):
#     username = request.data.get('username')
#     sleeper_user = SleeperUser.objects.get(username=username)
#     serializer = SleeperUserSerializer(sleeper_user)
#     return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
# # Function-based views(DevCodeCamp's lesson plan)
# class LoginView(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = SleeperUserSerializer
#     def get(self,request, *arg, **kwargs):
#         username = request.GET.get('username')
#         try:
#             sleeper_user= SleeperUser.objects.get(username=username)
#         except SleeperUser.DoesNotExist:
#             return Response({'error': 'Username Not Found'}, status=status.HTTP_400_BAD_REQUEST)
#         serializer = SleeperUserSerializer(sleeper_user)
#         return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
# # generic.APIView form of login request☝️
