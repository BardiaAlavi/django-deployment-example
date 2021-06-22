from django.shortcuts import render
from App import models, forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def index(request):

    user_lists=User.objects.order_by('email')
    registered=False

    if request.method=='POST':

        user_main=forms.mainform(data=request.POST)
        user_pic=forms.subform(data=request.POST)

        if user_main.is_valid() and user_pic.is_valid():
            user=user_main.save()
            user.set_password(user.password)
            user.save(commit=True)

            pic=user_pic.save(commit=False)

            pic.user=user

            if 'images' in request.FILES:
                pic.images= request.FILES['images']
                pic.save(commit=True)
                registered=True

        else:
            print(user_main.errors, user_pic.errors)
    else:
        user_main=forms.mainform()
        user_pic=forms.subform()

    return render(request, 'App/index.html', {'registered': registered, 'user_lists':user_lists, 'user_main': user_main, 'user_pic': user_pic})

from django.http import HttpResponseRedirect, HttpResponse

def Log_in(request):

    if request.method=='POST':

        user_main=forms.mainform(data=request.POST)
        user_pic=forms.subform(data=request.POST)

        if user_main.is_valid() and user_pic.is_valid():
            user=user_main.save()
            user.set_password(user.password)
            user.save(commit=True)

            pic=user_pic.save(commit=False)

            pic.user=user

            if 'images' in request.FILES:
                pic.images= request.FILES['images']
                pic.save(commit=True)
                registered=True

        else:
            print(user_main.errors, user_pic.errors)
    else:
        user_main=forms.mainform()
        user_pic=forms.subform()
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username, password=password)
        if user:
            if user.is_active():
                login(request, user)

                print('worked')

                return HttpResponseRedirect(reverse('index'))
            else:

                return HttpResponse('user not active')
        else:
            print("DANGER")

    else:
        return render(request, 'App/login.html', {'user_main': user_main, 'user_pic': user_pic})

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))


# Create your views here.
