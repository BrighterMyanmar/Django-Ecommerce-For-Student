from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name

class SubCat(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    parent = models.ForeignKey(Category,on_delete=models.CASCADE)

# create Model 
# makemigrations 
# migrate
# Register model inside admin.py

#car 
    # -Toyota
    # -Tesla
    # -Suziki
