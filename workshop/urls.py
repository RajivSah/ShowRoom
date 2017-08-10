from django.conf.urls import url
from .import views
app_name = 'workshop'
urlpatterns=[
    #/workshop/
    url(r'^$', views.workshop_list_view.as_view(), name='Workshop'),
    url(r'^details/(?P<pk>\d+)$', views.workshop_detail_view.as_view(), name='Workshop_details'),
    url(r'^addrecord/$', views.workshop_add_view.as_view(), name='Workshop_addrecords'),

    #/workshop/add_records/
    #url(r'^()$',)
]