from django.shortcuts import render
from rest_framework import viewsets
from category.models import Category
from product.models import Product
from .serializer import CategorySerializer,ProductSerializer
from rest_framework import permissions

class CategoryView(viewsets.ModelViewSet) :
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly] # get post ptach delete
    #http_method_names = ['get','post','patch','delete']

class ProductView(viewsets.ModelViewSet) :
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
