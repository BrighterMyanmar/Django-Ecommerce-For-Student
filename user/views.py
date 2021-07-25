from django.shortcuts import render,redirect
from django.http import HttpResponse;
from .froms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST" :
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Register Sucess Mr.{username}, please login!')
            return redirect('/user/login/')
    else :
        form = UserRegisterForm()
    
    return render(request,'user/register.html',{'form':form})

# @123!Abc
