from django.shortcuts import render
from rest_framework import viewsets
from category.models import Category
from product.models import Product
from .serializer import CategorySerializer,ProductSerializer

class CategoryView(viewsets.ModelViewSet) :
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer

class ProductView(viewsets.ModelViewSet) :
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
