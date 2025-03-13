from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

# API Overview view
@api_view(["GET"])
def Apioverview(request):
    api_urls = {
        "all_product": "/",
        "add_product": "/AddProduct",
        "update_product": "/update/<pk>",
        "delete_product": "/product/<pk>/delete",
    }
    return Response(api_urls)

# List all products and create a new product
class AllProductview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Add a new product (this is handled by ListCreateAPIView, no need for a separate class)
class AddProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Update an existing product
class UpdateProduct(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    partial=True
    lookup_field = 'pk'  # Ensures that the pk is used to identify the product for updating
