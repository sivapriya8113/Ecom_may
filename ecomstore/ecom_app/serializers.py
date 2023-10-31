from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


# class CustomTokenObtainPairSerailizer(TokenObtainSerializer):
#     def validate(self,attrs):
#         data = super(CustomTokenObtainPairSerailizer,self).validate(attrs)
#         user = UserSerializer(self.user)
#         data.update({'user':user.data})
#         return data