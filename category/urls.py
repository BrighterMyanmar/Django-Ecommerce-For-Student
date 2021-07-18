from django.urls import path
from .views import *

urlpatterns = [
    path('',cats,name='all-cats'),
    path('subs/',subs,name='all-subs')
]

