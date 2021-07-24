from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Category,SubCat;
from .forms import SubCatForm

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

def subCarte(request) :
    if request.method == "POST" : 
        form = SubCatForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('/cats/subs/')
    else : 
        form = SubCatForm()
        
    return render(request,'category/create.html',{'title':"Create Sub Category",'form':form});

def subEdit(request,id):
    subcat = SubCat.objects.get(pk=id)
    if request.method == "POST" :
        form = SubCatForm(request.POST,request.FILES,instance=subcat)
        if form.is_valid():
            form.save() 
            return redirect('/cats/subs/')
    else :
        form = SubCatForm(instance=subcat)
        
    return render(request,'category/edit.html',{'form':form})

def subDelete(request,id):
    subcat = SubCat.objects.get(pk=id)
    subcat.delete()
    return redirect('/cats/subs/')
