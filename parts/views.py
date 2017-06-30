from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from . import models
from . import forms
from django.http import HttpResponseRedirect

def populate_nav_bar():
    gly_name = ['glyphicon glyphicon-plus', 'glyphicon glyphicon-log-out']
    link_list = [reverse('parts:part_add'), reverse('main:login_page',args=[0])]
    link_name = ['Add Part', 'Log Out']
    my_list = zip(gly_name, link_list, link_name)
    return my_list


def parts_home(request):
    my_list=populate_nav_bar()
    part_list_= models.part_list.objects.all()
    return render(request,'parts.html',{'part_list': part_list_,'my_list': my_list})



def part_add_view(request):
    my_list=populate_nav_bar()
    return render(request,'part_add.html',{'form':forms.part_add_form,'my_list':my_list})


def part_add_validate(request):
    if request.method  == 'POST':
        form_entered=forms.part_add_form(request.POST)
        if form_entered.is_valid():
            temp = models.part_list()
            temp.part_id=form_entered.cleaned_data['part_id']
            temp.part_name=form_entered.cleaned_data['part_name']
            temp.cost=0 if (form_entered.cleaned_data['cost'] == None ) else form_entered.cleaned_data['cost']
            temp.save()
            return HttpResponseRedirect(reverse('parts:parts_home'))
    else:
        pass

def part_details(request,pk):
    my_list=populate_nav_bar()
    temp=models.part_list.objects.get(part_id=pk)
    return render(request,'part_details.html',{'part_temp':temp,'my_list':my_list})


def part_search(request,text):
    my_list=populate_nav_bar()
    temp=models.part_list.objects.filter(Q(part_id__icontains=text) | Q(part_name__icontains=text))
    return render(request,'part_search.html',{'part_list':temp,'my_list':my_list,})


def part_search(request):
    my_list= populate_nav_bar()
    text=request.GET.get('search_text')
    temp=models.part_list.objects.filter(Q(part_id__icontains=text) | Q(part_name__icontains=text))
    return render(request,'part_search.html',{'part_list':temp,'my_list':my_list,})

