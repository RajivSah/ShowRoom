from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import part_list, part_stock, applicable_model
from .forms import part_stock_form, applicable_form


def populate_nav_bar():
    gly_name = ['glyphicon glyphicon-plus', 'glyphicon glyphicon-log-out']
    link_list = [ reverse('parts:part_add_view'), reverse('main:logout')]
    link_name = ['Add Part', 'Log Out']
    my_list = zip(gly_name, link_list, link_name)
    return my_list

class part_list_view(ListView):
    model = part_list
    context_object_name = 'part_list'
    template_name = 'part_list.html'

    def get_context_data(self, **kwargs):
        context = super(part_list_view, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp != True:
            return HttpResponseRedirect(temp)
        else:
            return super(part_list_view,self).get(request,*args, **kwargs)

class part_detail_view(DetailView):
    model = part_list
    context_object_name = 'part_detail'
    template_name = 'part_detail.html'

    def get_context_data(self, **kwargs):
        context = super(part_detail_view, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        context['form'] = part_stock_form()
        context['app_add_form'] = applicable_form()
        self.request.session['part_id'] = self.kwargs['pk']
        self.request.session.modified = True
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp != True:
            return HttpResponseRedirect(temp)
        else:
            return super(part_detail_view,self).get(request,*args, **kwargs)

class part_add_view(CreateView):
    model = part_list
    fields = ['part_id','part_name','cost']
    template_name = 'part_add.html'
    success_url = reverse_lazy('parts:part_list')

    def get_context_data(self, **kwargs):
        context = super(part_add_view, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp != True:
            return HttpResponseRedirect(temp)
        else:
            return super(part_add_view,self).get(request,*args, **kwargs)

class part_update_view(UpdateView):
    model = part_list
    fields = ['part_id','part_name','cost']
    template_name = 'part_add.html'
    success_url = reverse_lazy('parts:part_list')

    def get_context_data(self, **kwargs):
        context = super(part_update_view, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp != True:
            return HttpResponseRedirect(temp)
        else:
            return super(part_update_view,self).get(request,*args, **kwargs)



class stock_add_view(CreateView):
    model = part_stock
    fields = ['part_id','entry_date','supplier','amount','remaining']
    success_url = reverse_lazy('parts:part_list')
    template_name = 'part_detail.html'

    def get_context_data(self, **kwargs):
        context = super(stock_add_view,self).get_context_data(**kwargs)
        if 'part_id' in self.request.session:
            context['part_detail'] = part_list.objects.get(pk=self.request.session['part_id'])
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp != True:
            return HttpResponseRedirect(temp)
        else:
            return super(stock_add_view,self).get(request,*args, **kwargs)


class stock_update_view(UpdateView):
    model = part_stock
    fields = ['part_id','entry_date','supplier','amount','remaining']
    success_url = reverse_lazy('parts:part_list')
    template_name = 'part_stock_form.html'

    def get_context_data(self, **kwargs):
        context = super(stock_update_view, self).get_context_data(**kwargs)
        context['update_form'] = context.get('form')
        return context

    def form_invalid(self, form):
        return render(self.request, 'part_detail.html', {'form':part_stock_form(),'update_form': form, 'part_detail': part_list.objects.get(pk=self.request.session['part_id'])})

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp != True:
            return HttpResponseRedirect(temp)
        else:
            return super(stock_update_view,self).get(request,*args, **kwargs)

class stock_delete_view(DeleteView):
    model = part_stock
    success_url = reverse_lazy('parts:part_list')
    template_name = 'part_stock_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(stock_delete_view, self).get_context_data(**kwargs)
        context['delete_form'] = context.get('form')
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp != True:
            return HttpResponseRedirect(temp)
        else:
            return super(stock_delete_view,self).get(request,*args, **kwargs)

class part_search_view(ListView):
    model = part_list
    context_object_name = 'part_list'
    template_name = 'part_list.html'

    def get_context_data(self, **kwargs):
        context = super(part_search_view, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context

    def get_queryset(self):
        key = self.request.GET['search_text']
        partlist = part_list.objects.filter(Q(part_id__icontains=key) | Q(part_name__icontains=key))
        return partlist

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp != True:
            return HttpResponseRedirect(temp)
        else:
            return super(part_search_view,self).get(request,*args, **kwargs)


class app_add_view(CreateView):
    model = applicable_model
    fields = ['partId', 'applicable']
    success_url = reverse_lazy('parts:part_list')
    template_name = 'part_detail.html'

    def get_context_data(self, **kwargs):
        context = super(app_add_view, self).get_context_data(**kwargs)
        if 'part_id' in self.request.session:
            context['part_detail'] = part_list.objects.get(pk=self.request.session['part_id'])
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp != True:
            return HttpResponseRedirect(temp)
        else:
            return super(app_add_view,self).get(request,*args, **kwargs)

class app_update_view(UpdateView):
    model = applicable_model
    fields = ['partId', 'applicable']
    success_url = reverse_lazy('parts:part_list')
    template_name = 'app_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(app_update_view, self).get_context_data(**kwargs)
        context['app_update_form'] = context.get('form')
        return context

    def form_invalid(self, form):
        return render(self.request, 'part_detail.html', {'app_add_form':applicable_form(),'app_update_form': form, 'part_detail':  part_list.objects.get(pk=self.request.session['part_id'])})

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp != True:
            return HttpResponseRedirect(temp)
        else:
            return super(app_update_view,self).get(request,*args, **kwargs)

class app_delete_view(DeleteView):
    model = applicable_model
    success_url = reverse_lazy('parts:part_list')
    template_name = 'app_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(app_delete_view, self).get_context_data(**kwargs)
        if 'part_id' in self.request.session:
            context['part_detail'] = part_list.objects.get(pk=self.request.session['part_id'])
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp != True:
            return HttpResponseRedirect(temp)
        else:
            return super(app_delete_view,self).get(request,*args, **kwargs)


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