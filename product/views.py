from django.shortcuts import render
from .models import Product 
from django.core.serializers.json import DjangoJSONEncoder
import json

def products(request):
    products = Product.objects.all();
    context = {
        'products':Product.objects.all()
    }
    return render(request,'product/index.html',context)

def cartview(request,ost): # "1,2,3,4,5"
    productList = ost.split(',') # [1,2,3,4,5]
    products = Product.objects.filter(pk__in=productList).values('id','name','price','image')
    product = json.dumps(list(products),cls=DjangoJSONEncoder)
    return render(request,'product/cartview.html',{'product':product})
