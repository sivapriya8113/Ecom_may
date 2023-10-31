from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.

"""
Prodcut =  list
           details
           add to cart
           search
           remove from cart 
           Payment gateway
"""
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics


class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data)

