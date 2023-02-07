from rest_framework import serializers
from .models import SleeperUser
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# class SleeperTokenSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         # for any additional fields you'd like to add to the JWT sent back in response
#         # add below using the token["field name"] = user.name_of_property
#         # token["is_student"] = user.is_student

#         token["username"] = user.username
#         token["password"] = user.password

#         return token
    
class SleeperUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[
                                   UniqueValidator(queryset=SleeperUser.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = SleeperUser
        fields = ['username', 'password']

    def get(self, validated_data):

        user = SleeperUser.objects.get(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


# class SleeperUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SleeperUser
#         fields = ['id', 'username', 'password']