from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import *
from django.urls import reverse


def populate_nav_bar():
    gly_name = ['glyphicon glyphicon-plus', 'glyphicon glyphicon-log-out']
    link_list = [ reverse('customer:customer_add'), reverse('main:logout')]
    link_name = ['Register Customer', 'Log Out']
    my_list = zip(gly_name, link_list, link_name)
    return my_list

class list_customer(ListView):
    model = customer_info
    template_name = 'customer_list.html'
    context_object_name = 'customer_list'

    def get_context_data(self, **kwargs):
        context = super(list_customer, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context


class add_customer(CreateView):
    model = customer_info
    template_name = 'customer_add.html'
    success_url = reverse_lazy('customer:customer_list')
    fields = ['fName','lName','phone','add_city','add_dist','gender']

    def get_context_data(self, **kwargs):
        context = super(add_customer, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

class deail_customer(DetailView):
    model = customer_info
    template_name = 'customer_detail.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super(deail_customer, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

class update_customer(UpdateView):
    model = customer_info
    template_name = 'customer_add.html'
    fields = ['fName','lName','phone','add_city','add_dist','gender']
    success_url = reverse_lazy('customer:customer_list')

    def get_context_data(self, **kwargs):
        context = super(update_customer, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context


class search_customer(ListView):
    model = customer_info
    template_name = 'customer_list.html'
    context_object_name = 'customer_list'

    def get_context_data(self, **kwargs):
        context = super(search_customer, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

    def get_queryset(self):
        key = self.request.GET['search_text']
        q = Q()
        for term in key.split():
            q = q | Q(fName__icontains=term) | Q(lName__icontains=term)
        return customer_info.objects.filter(q)


