from django.urls import path,include 
from rest_framework import routers 
from . import views 

route = routers.DefaultRouter() 
route.register('cats',views.CategoryView)
route.register('products',views.ProductView)


urlpatterns = [
    path('',include(route.urls))
]


# api/cats -> get
# api/cats/id -> get 
# cats/ post -> Create new category
# cats/ patch -> Update Category
