from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from vehicle_models.models import customer_vehicle_info
from .models import part_list, part_stock, applicable_model,part_processing
from .forms import part_stock_form, applicable_form,part_processing_form
from customer.models import customer_info
from customer.forms import cstm_add_form



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
        if temp == True :
            return super(part_list_view, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)

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
        if temp == True :
            return super(part_detail_view, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)

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
        if temp == True :
            return super(part_add_view, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)

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
        if temp == True :
            return super(part_update_view, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)



class stock_add_view(CreateView):
    model = part_stock
    fields = ['part_id','entry_date','supplier','amount']
    template_name = 'part_detail.html'

    def get_context_data(self, **kwargs):
        context = super(stock_add_view,self).get_context_data(**kwargs)
        if 'part_id' in self.request.session:
            context['part_detail'] = part_list.objects.get(pk=self.request.session['part_id'])
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp == True :
            return super(stock_update_view, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)

    def get_success_url(self):
        return reverse('parts:part_detail',args=[self.request.session['part_id']])

    def post(self, request, *args, **kwargs):
        form = part_stock_form(request.POST)
        if form.is_valid():
            part_id = form.cleaned_data['part_id']
            amount = form.cleaned_data['amount']
            temp = part_list.objects.get(part_id = part_id)
            temp.available_quantity+=amount
            temp.save()

        return super(stock_add_view,self).post(request,*args, **kwargs)

class stock_update_view(UpdateView):
    model = part_stock
    fields = ['part_id','entry_date','supplier','amount']
    template_name = 'part_stock_form.html'

    def get_context_data(self, **kwargs):
        context = super(stock_update_view, self).get_context_data(**kwargs)
        context['update_form'] = context.get('form')
        return context

    def form_invalid(self, form):
        return render(self.request, 'part_detail.html', {'form':part_stock_form(),'update_form': form,'app_add_form':applicable_form(), 'part_detail': part_list.objects.get(pk=self.request.session['part_id'])})

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp == True :
            return super(stock_update_view, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)

    def get_success_url(self):
        return reverse('parts:part_detail', args=[self.request.session['part_id']])

    def post(self, request, *args, **kwargs):
        form = part_stock_form(request.POST)
        if form.is_valid():
            part_id = form.cleaned_data['part_id']
            amount = form.cleaned_data['amount']
            temp = part_list.objects.get(part_id = part_id)
            temp2 =part_stock.objects.get(pk = self.kwargs['pk'])
            prevAmount = temp2.amount
            temp.available_quantity+=amount-prevAmount
            temp.save()

        return super(stock_update_view,self).post(request,*args, **kwargs)


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
        if temp == False:
            if temp == True:
                return super(stock_delete_view, self).get(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(temp)

    def post(self, request, *args, **kwargs):
        temp =part_stock.objects.get(pk = self.kwargs['pk'])
        temp2 = part_list.objects.get(part_id=temp.part_id)
        temp2.available_quantity-=temp.amount
        temp2.save()
        return super(stock_delete_view,self).post(request,*args, **kwargs)

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
        if temp == True :
            return super(part_search_view, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)


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
        if temp == True :
            return super(app_add_view, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)

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
        if temp == True :
            return super(app_update_view, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)

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
        if temp == True :
            return super(app_update_view, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)


def ajax_customer_search(request):
    if request.is_ajax():
        q =request.GET.get('q')
        if q is not None:
            results = customer_vehicle_info.objects.filter(
                Q(VRN__icontains=q)|
                Q(customerId__fName__icontains=q)
            )

            return render(request, 'results.html', {'results':results,'part_pro_form' : part_processing_form(),'part_id': request.session["part_id"]})

def index(request):
    return render(request, 'index.html', {})


class parts_processing(TemplateView):
    template_name = 'parts_processing.html'

    def get_context_data(self, **kwargs):
        context = super(parts_processing, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        if 'part_id' in self.request.session:
            context['part_detail'] = part_list.objects.get(pk=self.request.session['part_id'])
        context['part_pro_form'] = part_processing_form()
        return context
    
    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp == True :
            return super(parts_processing, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)

class PartProAdd(CreateView):
    model = part_processing
    fields = ['pID', 'out_date', 'req_form_no', 'quantity', 'vehicle_id']
    success_url = reverse_lazy('parts:part_list')
    template_name = 'parts_processing.html'

    def get_context_data(self, **kwargs):
        context = super(PartProAdd, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        if 'part_id' in self.request.session:
            context['part_detail'] = part_list.objects.get(pk=self.request.session['part_id'])
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp == True :
            return super(PartProAdd, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)

    def post(self, request, *args, **kwargs):
        form = part_processing_form(request.POST)
        if form.is_valid():
            part_id = form.cleaned_data['pID']
            amount = form.cleaned_data['quantity']
            temp = part_list.objects.get(part_id = part_id)
            temp.available_quantity-=amount
            temp.save()

        return super(PartProAdd,self).post(request,*args, **kwargs)


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