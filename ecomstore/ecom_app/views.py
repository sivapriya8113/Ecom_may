from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer,UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.


class Register(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        user = serializer.create(serializer.validated_data)


        return Response(data,status=status.HTTP_201_CREATED)


# class MyTokenObtainPair(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerailizer



"""
Class based api views 


mixins 
API View
Viewset 
generics - 

function based 
decorator 
@api_view[]

"""

