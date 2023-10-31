from django.urls import path
from . views import ListProduct

urlpatterns = [
    path('product-list',ListProduct.as_view(),name = 'list')

]