from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import *
from django.urls import reverse
from . import forms
from . import models


def login_validate(request):
    if 'department' in request.session:
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

            if check:
                # print('valid login')
                # check the type of user
                request.session['department'] = check['department']
                # request.session['user'] = check['object'].username
                request.session.modified = True
                obj = check_session(request)
                return HttpResponseRedirect(obj)
            else:
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
    if 'part_id' in request.session:
        del request.session['part_id']
        request.session.modified = True
    return HttpResponseRedirect(reverse('main:login_page'))


def check_session(request):
    if request.session['department'] == "administration":
        return reverse('admin')
    elif request.session['department'] == "parts":
        return reverse('parts:part_list')
    elif request.session['department'] == "workshop":
        return reverse('workshop:Workshop')
    elif request.session['department'] == "showrooms":
        return reverse('showrooms:manufacturerLists')

    else:
        return reverse('main:login_page')





def populate_nav_bar():
    gly_name = ['glyphicon glyphicon-plus', 'glyphicon glyphicon-log-out']
    link_list = [ reverse('main:employee_add'), reverse('main:logout')]
    link_name = ['Register employee', 'Log Out']
    my_list = zip(gly_name, link_list, link_name)
    return my_list

class list_employee(ListView):
    model = employee
    template_name = 'employee_list.html'
    context_object_name = 'employee_list'

    def get_context_data(self, **kwargs):
        context = super(list_employee, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context


class add_employee(CreateView):
    model = employee
    template_name = 'employee_add.html'
    success_url = reverse_lazy('main:employee_list')
    fields = ['first_name','last_name','address_city','address_district','contact','salary','department_id','Gender','joined_date']

    def get_context_data(self, **kwargs):
        context = super(add_employee, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

class deail_employee(DetailView):
    model = employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        context = super(deail_employee, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

class update_employee(UpdateView):
    model = employee
    template_name = 'employee_add.html'
    fields = ['first_name','last_name','address_city','address_district','contact','salary','department_id','Gender','joined_date']
    success_url = reverse_lazy('main:employee_list')

    def get_context_data(self, **kwargs):
        context = super(update_employee, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context


class search_employee(ListView):
    model = employee
    template_name = 'employee_list.html'
    context_object_name = 'employee_list'

    def get_context_data(self, **kwargs):
        context = super(search_employee, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

    def get_queryset(self):
        key = self.request.GET['search_text']
        q = Q()
        for term in key.split():
            q = q | Q(first_name__icontains=term) | Q(last_name__icontains=term)
        return employee.objects.filter(q)