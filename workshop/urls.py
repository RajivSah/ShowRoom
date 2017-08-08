from django.conf.urls import url
from .import views

urlpatterns=[
    #/workshop/
    url(r'^$', views.index, name='Workshop'),
    #/workshop/add_records/
    #url(r'^()$',)
]