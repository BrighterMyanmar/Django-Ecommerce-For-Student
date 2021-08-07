from django.db import models
from category.models import Category,SubCat
from user.models import User

class Product(models.Model) :
    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField() 
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcat = models.ForeignKey(SubCat,on_delete=models.CASCADE)

class Orders(models.Model):
    count = models.IntegerField() 
    total = models.IntegerField() 
    userId = models.ForeignKey(User,on_delete=models.CASCADE)

class OrderItems(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField() 
    image = models.CharField(max_length=225) 
    count = models.IntegerField() 
    orderId = models.ForeignKey(Orders,on_delete=models.CASCADE)
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
