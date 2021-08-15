from rest_framework import serializers
from category.models import Category
from product.models import Product

class CategorySerializer(serializers.HyperlinkedModelSerializer) :
    class Meta : 
        model = Category
        fields = ['id','url','name','image']

class ProductSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Product
        fields = ['id','name','image','price','category','subcat']

