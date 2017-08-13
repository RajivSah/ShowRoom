from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView
from django.urls import reverse,reverse_lazy
from .models import *
from .forms import *
from django.http import HttpResponse,request
from django.db.models import F


def processImport(request):

        if request.method == 'POST':
            form = ImportDetailsForm(request.POST)
            if form.is_valid():
                quantityRev = form.cleaned_data['quantity']
                colorRev = form.cleaned_data['color']
                modelRev = form.cleaned_data['model']
                form.save()
                stock=ModelStock.objects.filter(model=modelRev,color=colorRev)
                if not stock:
                    modelStock=ModelStock.objects.create(model=modelRev,color=colorRev,quantity=quantityRev)
                    return HttpResponse("new stock created")
                else:
                    stock = ModelStock.objects.filter(model=modelRev, color=colorRev).update(quantity=F('quantity')+quantityRev)
                    return  HttpResponse("Stock Updated")




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
        context['VehicleName'] = VehicleNameForm(self.request.POST, self.request.FILES)
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
    fields = ['category','vehicleName','image']

    def get_context_data(self, **kwargs):
        context = super(AddVehicleName, self).get_context_data(**kwargs)
        return context

    '''
    def addVehicle(request):

    if request.method == 'POST':

        form = VehicleNameForm(request.POST,request.FILES)
        form1= VehicleNameForm(request.POST)
        if form.is_valid():
            category=form.cleaned_data['category']
            name=form.cleaned_data['vehicleName']
            image=form.cleaned_data['image']
            form.save()
            return HttpResponse(image)

    else:
        form = VehicleNameForm()
        form1 = VehicleNameForm()

    return render(request, 'add_model.html', {'VehicleNameForm': form,'VehicleName':form1})

    
    '''


class AddModels(CreateView):
    model = VehicleModels
    template_name = 'add_model.html'
    success_url = reverse_lazy('vehicle_models:add_model')
    fields = ['vehicleName','model','image']

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

