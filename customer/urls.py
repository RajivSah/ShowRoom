from django.conf.urls import url
from .views import *
app_name='customer'

urlpatterns=[
    url(r'^customer_list/$',list_customer.as_view(),name='customer_list'),
    url(r'^customer_detail/(?P<pk>\d+)/$',deail_customer.as_view(),name='customer_detail'),
    url(r'^customer_add/$',add_customer.as_view(),name='customer_add'),
    url(r'^customer_update/(?P<pk>\d+)$',update_customer.as_view(),name='customer_update'),
    url(r'^customer_search/',search_customer.as_view(),name='customer_search'),
]