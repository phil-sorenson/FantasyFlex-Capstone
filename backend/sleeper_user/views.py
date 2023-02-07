# from rest_framework.authentication import TokenAuthentication
# from rest_framework.views import APIView
# from django.shortcuts import render
# from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from django.shortcuts import get_object_or_404
from rest_framework import status
# from django.contrib.auth import get_user_model
from rest_framework import generics
# from .models import SleeperUser
from .serializers import SleeperUserSerializer
# from authentication.serializers import MyTokenObtainPairSerializer
from sleeper_wrapper import User



# AUTH LOGIN ROUTE -- (POST) - Create a token if credentials match ('/sleeperlogin')
# class LoginView(generics.CreateAPIView):
#     serializer_class = SleeperUserSerializer

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def login_user(self, request, *args, **kwargs):
    serializer = self.get_serializer(data = request.data)
    if serializer.is_valid():
        user = request.user.save()
        return Response({
            "user": SleeperUserSerializer (user,context=self.get_serializer_context().data,
            status = status.HTTP_201_CREATED)
            })
    return Response(serializer.errors, status=status.HTTP_401_BAD_REQUEST)

# class GetSleeperUser(generics.RetrieveAPIView):
#     SleeperUser = User.get_user(self)
#     queryset = User.get_user(self)
#     serializer_class = SleeperUserSerializer
#     lookup_field = ('user_id' , 'username')
# ROUTE TO GET USER AFTER LOGGED IN  ('/user/<:user_id>')
@api_view(['GET'])
@permission_classes([AllowAny])
def UserData(user):
    user_id = User.get_user_id(user_id)
    user = User.get_user()


    # try:
    #     user = SleeperUser.objects.get(id=id)
    #     return Response({
    #         'user_id': user.id,
    #         'username': user.username
    #     }, status= status.HTTP_200_OK)
    # except SleeperUser.DoesNotExist:
    #     return Response({"error":'No User Found'}, status=status.HTTP_404_NOT_FOUND)


