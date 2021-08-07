from django.contrib import admin
from .models import Product,Orders,OrderItems

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderItems)
