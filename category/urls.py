from django.urls import path
from .views import *

urlpatterns = [
    path('',cats,name='all-cats'),
    path('subs/',subs,name='all-subs'),
    path('subs/create/',subCarte,name='sub-create'),
    path('subs/<int:id>/edit',subEdit,name="sub-edit"),
    path('subs/<int:id>/delete',subDelete,name="sub-delete"),
]


