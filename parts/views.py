from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
from . import models
from . import forms
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse


def populate_nav_bar():
    gly_name = ['glyphicon glyphicon-plus', 'glyphicon glyphicon-log-out']
    link_list = [reverse('parts:part_add'), reverse('main:logout')]
    link_name = ['Add Part', 'Log Out']
    my_list = zip(gly_name, link_list, link_name)
    return my_list

def check_session_exist(request):
    try:
        department= request.session['department']
        if department != 'parts':
            raise ValueError
        return True
    except KeyError:
        return (reverse('main:login_page'))
    except ValueError:
        return (reverse('main:login_page'))


def parts_home(request):
    temp =check_session_exist(request)
    if temp != True:
        return HttpResponseRedirect(temp)

    my_list=populate_nav_bar()
    part_list_= models.part_list.objects.all()
    return render(request,'parts.html',{'part_list': part_list_,'my_list': my_list})



def part_add_view(request):
    temp =check_session_exist(request)
    if temp != True:
        return HttpResponseRedirect(temp)

    my_list=populate_nav_bar()
    return render(request,'part_add.html',{'form':forms.part_add_form,'my_list':my_list})


def part_add_validate(request):
    if request.method  == 'POST':
        form_entered=forms.part_add_form(request.POST)
        print(form_entered)
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
    temp =check_session_exist(request)
    if temp != True:
        return HttpResponseRedirect(temp)

    my_list=populate_nav_bar()
    temp_list = models.part_list.objects.get(part_id=pk)

    if request.method  == 'POST':
        form_entered=forms.part_stock_form(request.POST,prefix='add')
        if form_entered.is_valid():
            temp = models.part_stock()
            temp.part_id = models.part_list.objects.get(pk=pk)
            temp.entry_date = form_entered.cleaned_data['entry_date']
            temp.supplier = form_entered.cleaned_data['supplier']
            temp.amount = form_entered.cleaned_data['amount']
            temp.save()
            return HttpResponseRedirect(reverse('parts:part_details',args=[pk]))
        else:
            return render(request, 'part_details.html',
                          {'part_temp': temp_list, 'my_list': my_list, 'part_stock_form': form_entered,'part_stock_edit':forms.part_stock_form(prefix='edit')})

    return render(request,'part_details.html', {'part_temp':temp_list,'my_list':my_list,'part_stock_form': forms.part_stock_form(prefix='add'),'part_stock_edit':forms.part_stock_form(prefix='edit')})



def stock_edit(request):
    temp = check_session_exist(request)
    if temp != True:
        return HttpResponseRedirect(temp)

    stock_id = request.GET.get('stock_id')
    entry_date= request.GET.get('entry_date')
    supplier = request.GET.get('supplier')
    amount = request.GET.get(('amount'))
    data={'stock_id':stock_id,'entry_date':entry_date,'supplier':supplier,'amount':amount}
    form_entered = forms.part_stock_form()
    form_entered.entry_date = entry_date
    form_entered.supplier = supplier
    form_entered.amount = amount

    part = models.part_stock.objects.get(id=stock_id)
    temp_model = models.part_stock(id=stock_id,part_id=part.part_id,entry_date=entry_date,supplier=supplier,amount=amount)
    temp_model.save()
    return JsonResponse(data)

def app_save(request):
    temp =check_session_exist(request)
    if temp != True:
        return HttpResponseRedirect(temp)

    if request.method == "POST":
        form_entered = forms.applicable_form(request.POST)
        print(form_entered)

    return HttpResponseRedirect(reverse('parts:part_details'))




# def part_stock_add_validate(request,pk):
#     if request.method  == 'POST':
#         form_entered=forms.part_stock_form(request.POST)
#         if form_entered.is_valid():
#             temp = models.part_stock()
#             temp.part_id = models.part_list.objects.get(pk=pk)
#             temp.entry_date = form_entered.cleaned_data['entry_date']
#             temp.supplier = form_entered.cleaned_data['supplier']
#             temp.amount = form_entered.cleaned_data['amount']
#             temp.save()
#             return HttpResponseRedirect(reverse('parts:part_details',args=[pk]))
#         else:
#             print("invalid field")
#             return HttpResponseRedirect(reverse('parts:part_details',args=[pk]))
#     else:
#         return HttpResponseRedirect(reverse('parts:part_details',args=[pk]))


def part_search(request):
    temp =check_session_exist(request)
    if not temp :
        return HttpResponseRedirect(temp)

    my_list= populate_nav_bar()
    text=request.GET.get('search_text')
    temp=models.part_list.objects.filter(Q(part_id__icontains=text) | Q(part_name__icontains=text))
    return render(request,'part_search.html',{'part_list':temp,'my_list':my_list,})


def part_app_model(request, pk):
    my_list = populate_nav_bar()
    temp_list = models.part_list.objects.get(part_id=pk)
    if request.method == 'POST':
        form_entered = forms.applicable_form(request.POST,prefix='add_app')
        if form_entered.is_valid():
            temp_model = models.applicable_model()
            temp_model.part_id = models.part_list.objects.get(pk=pk)
            temp_model.applicable = form_entered.cleaned_data['applicable']
            temp_model.save()
            return HttpResponseRedirect(reverse('parts:part_app_model', args=[pk] ))

        else:
            print("invalid")
            return render(request, 'part_app_model.html', {'part_temp': temp_list, 'my_list': my_list,
                                                           'add_app': form_entered,
                                                           'edit_app': forms.applicable_form(prefix= "edit_app")})

    return render(request,'part_app_model.html',{'part_temp':temp_list, 'my_list':my_list,'add_app':forms.applicable_form(prefix='add_app'),'edit_app':forms.applicable_form(prefix=
                                                                                                                                                      "edit_app")})