from django.db import models
from category.models import Category,SubCat

class Product(models.Model) :
    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField() 
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcat = models.ForeignKey(SubCat,on_delete=models.CASCADE)
