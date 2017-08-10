
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from vehicle_models.models import Manufacturer,VehicleCategory,VehicleName,VehicleModels,ModelDetails
from .models import Sales
from .forms import *


def populate_nav_bar():
    gly_name = ['glyphicon glyphicon-plus','glyphicon glyphicon-plus', 'glyphicon glyphicon-log-out']
    link_list = [reverse('showrooms:newSale'),reverse('vehicle_models:add_model'), reverse('main:logout')]
    link_name = ['New Sale','Add Model', 'Log Out']
    my_list = zip(gly_name, link_list, link_name)
    return my_list


def populate_nav_bar_sales():
    gly_name = ['glyphicon glyphicon-plus','glyphicon glyphicon-plus', 'glyphicon glyphicon-log-out']
    link_list = [reverse('showrooms:newSale'),reverse('customer:customer_add'), reverse('main:logout')]
    link_name = ['New Sale','New Customer', 'Log Out']
    my_list = zip(gly_name, link_list, link_name)
    return my_list


class ListSalesView(ListView):
    model = Sales
    context_object_name = 'sales_list'
    template_name = 'sales_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListSalesView, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar_sales()
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if not temp:
            return HttpResponseRedirect(temp)
        else:
            return super(ListSalesView, self).get(request, *args, **kwargs)


class NewSaleView(CreateView):
    model = Sales
    success_url = reverse_lazy('showrooms:newSale')
    template_name = 'sales.html'
    fields = ['customer','model','VIN','VRN','dateOfSale','soldRate']

    def get_context_data(self, **kwargs):
        context=super(NewSaleView, self).get_context_data(**kwargs)
        context['my_list']=populate_nav_bar_sales()
        context['newSaleForm']=SalesForm
        return context





class ManufacturerListView(ListView):
    model = Manufacturer
    context_object_name = 'manufacturer'
    template_name = 'manufacturer_list.html'

    def get_context_data(self, **kwargs):
        context = super(ManufacturerListView, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if not temp:
            return HttpResponseRedirect(temp)
        else:
            return super(ManufacturerListView,self).get(request,*args, **kwargs)

class CategoryListView(ListView):
    model = VehicleCategory
    context_object_name = 'category_list'
    template_name = 'category_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if not temp:
            return HttpResponseRedirect(temp)
        else:
            return super(CategoryListView,self).get(request,*args, **kwargs)

class VehicleNameListView(ListView):
    model = VehicleName
    context_object_name = 'vehicle_name_list'
    template_name = 'vehicle_name_list.html'



    def get_context_data(self, **kwargs):
        context = super(VehicleNameListView, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if not temp:
            return HttpResponseRedirect(temp)
        else:
            return super(VehicleNameListView,self).get(request,*args, **kwargs)

    def get_queryset(self):
        pk=self.kwargs['pk']
        return VehicleName.objects.filter(category=pk)


class ModelListView(ListView):
    model = VehicleModels
    context_object_name = 'model_list'
    template_name = 'model_list.html'

    def get_context_data(self, **kwargs):
        context = super(ModelListView, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if not temp:
            return HttpResponseRedirect(temp)
        else:
            return super(ModelListView,self).get(request,*args, **kwargs)

    def get_queryset(self):
        pk=self.kwargs['pk']
        return VehicleModels.objects.filter(vehicleName=pk)


class ModelDetailsView(DetailView):
    model = ModelDetails
    context_object_name = 'model_details'
    template_name = 'model_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ModelDetailsView, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if not temp:
            return HttpResponseRedirect(temp)
        else:
            return super(ModelDetailsView,self).get(request,*args, **kwargs)

    def get_queryset(self):
        pk=self.kwargs['pk']
        return ModelDetails.objects.filter(model=pk)



def check_session_exist(request):
    try:
        department= request.session['department']
        if department != 'showroom':
            raise ValueError
        return True
    except KeyError:
        return reverse('main:login_page')
    except ValueError:
        return reverse('main:login_page')