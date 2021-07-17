from django.shortcuts import render
from django.http import HttpResponse

def cats(request):
    context = {'title':"All Categories","content":"Page One"}
    return render(request,'category/cats.html',context)

def subs(request):
    return render(request,'category/subs.html',{'title':'All Sub Categories','content':"Page Two"})

def hey(request):
    return render(request,'category/hey.html',{'title':'Testing','content':'Page Three'})