from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import forms
from . import models

def login_page(request,login_status):
    return  render(request,'login.html',{'login_form':forms.login_form,'login_status':login_status})


def login_validate(request):
    # newContact = contact()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        login_info=forms.login_form(request.POST)

        # check whether it's valid:
        if login_info.is_valid():
            username_entered=login_info.cleaned_data['username']
            password_entered=login_info.cleaned_data['password']
            # print(username_entered,password_entered)
            check= models.user.objects.filter(password=password_entered)
            if check.count() == 1:
                return HttpResponseRedirect(reverse('home:home_page'))
            else:
                return  HttpResponseRedirect(reverse('main:login_page', args=[1]))
            # return HttpResponseRedirect(reverse('loggedIn'))
    # if a GET (or any other method) we'll create a blank form
    else:
        pass

    return render(request, 'login.html' )

def home_page(request):
    return render(request,'home.html')
