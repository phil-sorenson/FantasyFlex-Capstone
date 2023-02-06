from django.shortcuts import render
from .models import SleeperUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import MyTokenObtainPairSerializer, SleeperUserSerializer
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
User = get_user_model()



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LoginView(generics.CreateAPIView):
    queryset = SleeperUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SleeperUserSerializer



# AUTH LOGIN ROUTE -- (POST) - Create a token if credentials match ('/sleeperlogin')
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def login_user(request):
    serializer = SleeperUserSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ROUTE TO GET USER AFTER LOGGED IN  ('/user/<:user_id>')
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserData(request, id):
    try:
        user = SleeperUser.objects.get(id=id)
        return Response({
            'user_id': user.id,
            'username': user.username
        }, status= status.HTTP_200_OK)
    except SleeperUser.DoesNotExist:
        return Response({"error":'No User Found'}, status=status.HTTP_404_NOT_FOUND)


