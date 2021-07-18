from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,SubCat;

def cats(request):
    context = {
        'title':"All Categories",
        "content":"Page One",
        "cats":Category.objects.all()
    }
    return render(request,'category/cats.html',context)

def subs(request):
    return render(request,'category/subs.html',{
        'title':'All Sub Categories',
        'content':"Page Two",
        "subs":SubCat.objects.all()
        })
