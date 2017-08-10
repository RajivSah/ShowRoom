from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import job_records
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView,DetailView,CreateView
from .forms import jobrecord_form


def populate_nav_bar():
        gly_name = ['glyphicon glyphicon-plus', 'glyphicon glyphicon-log-out']
        link_list = [reverse('workshop:Workshop_addrecords'), reverse('main:logout')]
        link_name = ['Add Records', 'Log Out']
        my_list = zip(gly_name, link_list, link_name)
        return my_list
    #for i in all_records:
     #   url ='/workshop/' + str(i) + '/ '
     #   html += '<a href = "'+ url +'">'+ str(i.vid) +'</a><br>'


class workshop_list_view(ListView):
    model = job_records
    context_object_name = 'workshop_list'
    template_name = 'workshop.html'

    def get_context_data(self, **kwargs):
        context = super(workshop_list_view, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context



def check_session_exist(request):
    try:
        department= request.session['department']
        if department != 'workshop':
            raise ValueError
        return True
    except KeyError:
        return reverse('main:login_page')
    except ValueError:
        return reverse('main:login_page')

class workshop_detail_view(DetailView):
    model = job_records
    context_object_name = 'workshop_details'
    template_name = 'workshop_details.html'

    def get_context_data(self, **kwargs):
        context = super(workshop_detail_view, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        return context


    def get_queryset(self):
        pk=self.kwargs['pk']
        return job_records.objects.filter(id=pk )

class workshop_add_view(CreateView):
    model = job_records
    fields = ['vid','job_order','job_done','date','e_id']
    template_name = 'workshop_addrecords.html'
    success_url = reverse_lazy('workshop:Workshop')

    def get_context_data(self, **kwargs):

        context = super(workshop_add_view, self).get_context_data(**kwargs)
        context['my_list'] = populate_nav_bar()
        context['form'] = jobrecord_form
        return context


