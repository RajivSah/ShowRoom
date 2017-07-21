from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import *
from .forms import *

class add_model_first(CreateView):
    model = model_first
    template_name = 'add_model.html'
    success_url = reverse_lazy('vehicle_models:add_model')
    fields = ['manufacturer','product_name']

    def get_context_data(self, **kwargs):
        context = super(add_model_first,self).get_context_data(**kwargs)
        context['AddModelFirst'] = context.get('form')
        context['AddModelLast'] = model_last_form()
        return context


class add_model_last(CreateView):
    model = model_last
    template_name = 'add_model.html'
    success_url = reverse_lazy('vehicle_models:add_model')
    fields = ['modelFirst','model_last_name','color']

    def get_context_data(self, **kwargs):
        context = super(add_model_last,self).get_context_data(**kwargs)
        return context



