from django.conf.urls import url
from django.urls import reverse

from . import views

app_name='parts'
urlpatterns = [
    url(r'^$',views.part_list_view.as_view(),name='part_list'),
    url(r'^detail/(?P<pk>\d+)/$',views.part_detail_view.as_view(),name='part_detail'),
    url(r'^add$',views.part_add_view.as_view(),name='part_add_view'),
    url(r'^update/(?P<pk>\d+)/$',views.part_update_view.as_view(),name='part_update_view'),
    url(r'^add_stock/$',views.stock_add_view.as_view(),name='stock_add_view'),
    url(r'^update_stock/(?P<pk>\d+)/$',views.stock_update_view.as_view(),name='stock_update_view'),
    url(r'^delete_stock/(?P<pk>\d+)/$',views.stock_delete_view.as_view(),name='stock_delete_view'),
    url(r'^search/',views.part_search_view.as_view(),name='part_search_view'),
    url(r'^add_app/$',views.app_add_view.as_view(),name='app_add_view'),
    url(r'^update_app/(?P<pk>\d+)/$',views.app_update_view.as_view(),name='app_update_view'),
    url(r'^delete_app(?P<pk>\d+)/$',views.app_delete_view.as_view(),name='app_delete_view'),
]