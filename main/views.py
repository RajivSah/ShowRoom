from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login, authenticate



from . import forms
from . import models


def login_validate(request):
    # newContact = contact()
    if 'department' in request.session:
        print(request.session['department'])
        obj = check_session(request)
        return HttpResponseRedirect(obj)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        login_info = forms.login_form(request.POST)
        # check whether it's valid:
        if login_info.is_valid():
            username_entered = login_info.cleaned_data['username']
            password_entered = login_info.cleaned_data['password']
            # print(username_entered,password_entered)
            check = models.user.authenticate(password_entered, username_entered)
            print(check)
            if check:
                print('valid login')
                # check the type of user
                request.session['department'] = check['department']
                # request.session['user'] = check['object'].username
                request.session.modified = True
                obj = check_session(request)
                return obj
            else:
                print('invalid login')
                return render(request, 'login.html', {'login_form': forms.login_form, 'error': 1})

        else:
            pass

    return render(request, 'login.html', {'login_form': forms.login_form})


def home_page(request):
    return render(request, 'employee.html')


def logout(request):
    if request.session.has_key('department'):
        del request.session['department']
        request.session.modified = True
    return render(request, 'login.html', {'login_form': forms.login_form})


def check_session(request):
    print("in check_session")
    if request.session['department'] == "administration":
        return reverse('admin')
    elif request.session['department'] == "parts":
        print("in parts")
        return reverse('parts:parts_home')
    else:
        return reverse('main:login_page')
