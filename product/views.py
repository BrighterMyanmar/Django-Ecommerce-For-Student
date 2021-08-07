from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Orders, OrderItems
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

@login_required
def checkout(request,ost):
    order = saveOrder(request,ost)
    saveOrderItem(request,order,ost)
    messages.success(request,f'Order Successfully Saved!')
    return redirect('/')

def saveOrderItem(request,orderOb,ost):
    orderList = ost.split(',')
    for order in orderList : 
        proId = order.split(":")[0]
        proCount = order.split(":")[1]
        product = Product.objects.get(pk=proId)
        total = product.price * int(proCount);

        orderItem = OrderItems() 
        orderItem.name = product.name 
        orderItem.price = product.price 
        orderItem.image = product.image 
        orderItem.count = proCount
        orderItem.orderId = orderOb 
        orderItem.userId = request.user

        orderItem.save() 
    
    return True




def saveOrder(request,ost):
    orderList = ost.split(',')
    total = 0;
    for order in orderList :
        proId = order.split(":")[0]
        proCount = order.split(":")[1]
        product = Product.objects.get(pk=proId)
        total += product.price * int(proCount);
        
    order = Orders() 
    order.count = len(orderList)
    order.total = total
    order.userId = request.user
    order.save()
    return order;
