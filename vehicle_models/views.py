from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView
from django.urls import reverse,reverse_lazy
from .models import *
from .forms import *
from django.http import HttpResponse


def processImport(request):
    modelIn=request.POST['model']
    colorIn=request.POST['color']
    quantityIn=request.POST['quantity']
    importDatein=request.POST['importDate']
    ImportDetails.objects.create(model=modelIn,color=colorIn,quantity=quantityIn,importDate=importDatein)

    stock=ModelStock.objects.filter(model=modelIn)
    if not stock:
        exists='empty'
        ModelStock.objects.create(model=modelIn, color=colorIn, quantity=quantityIn)

    else:
        exists='found'
        rightModel=ModelStock.objects.get(model=modelIn,color=colorIn)
        qty=rightModel.quantity
        ModelStock.objects.create(model=modelIn, color=colorIn, quantity=qty+quantityIn)
    return  HttpResponse(str(exists))




def populate_nav_bar_sales():
    gly_name = ['glyphicon glyphicon-plus','glyphicon glyphicon-plus', 'glyphicon glyphicon-log-out']
    link_list = [reverse('showrooms:newSale'),reverse('customer:customer_add'), reverse('main:logout')]
    link_name = ['New Sale','New Customer', 'Log Out']
    my_list = zip(gly_name, link_list, link_name)
    return my_list


class AddModelImport(CreateView):
    model = ImportDetails
    template_name = 'add_model.html'
    success_url = reverse_lazy('vehicle_models:addImport')
    fields = ['model','color','quantity','importDate']

    def get_context_data(self, **kwargs):
        context = super(AddModelImport,self).get_context_data(**kwargs)
        return context






class UpdateManufacturer(UpdateView):
    model = Manufacturer
    fields = ['manufacturer']
    template_name = 'add_model.html'
    success_url = reverse_lazy('showrooms:manufacturerLists')

    def get_context_data(self, **kwargs):
        context = super(UpdateManufacturer, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar_sales()
        return context



class AddManufacturer(CreateView):
    model = Manufacturer
    template_name = 'add_model.html'
    success_url = reverse_lazy('vehicle_models:add_model')
    fields = ['manufacturer']

    def get_context_data(self, **kwargs):
        context = super(AddManufacturer,self).get_context_data(**kwargs)
        context['Manufacturer']=ManufacturerForm
        context['Category']=CategoryForm
        context['VehicleName'] = VehicleNameForm
        context['Model']=ModelForm
        context['ModelDetails']=ModelDetailsForm
        context['ImportDetails']=ImportDetailsForm
        return context


class AddVehicleCategories(CreateView):
    model = VehicleCategory
    template_name = 'add_model.html'
    success_url = reverse_lazy('vehicle_models:add_model')
    fields = ['manufacturer','category']

    def get_context_data(self, **kwargs):
        context = super(AddVehicleCategories,self).get_context_data(**kwargs)
        return context


class AddVehicleName(CreateView):
    model = VehicleName
    template_name = 'add_model.html'
    success_url = reverse_lazy('vehicle_models:add_model')
    fields = ['category','vehicleName']

    def get_context_data(self, **kwargs):
        context = super(AddVehicleName, self).get_context_data(**kwargs)
        return context


class AddModels(CreateView):
    model = VehicleModels
    template_name = 'add_model.html'
    success_url = reverse_lazy('vehicle_models:add_model')
    fields = ['vehicleName','model']

    def get_context_data(self, **kwargs):
        context = super(AddModels, self).get_context_data(**kwargs)
        return context


class AddModelDetails(CreateView):
    model = ModelDetails
    template_name = 'add_model.html'
    success_url = reverse_lazy('vehicle_models:add_model')
    fields = ['model','specs','availableQty']

    def get_context_data(self, **kwargs):
        context = super(AddModelDetails, self).get_context_data(**kwargs)
        return context

