from django.conf.urls import url
from . import views

app_name='parts'
urlpatterns = [
    url(r'^$',views.parts_home,name='parts_home'),
    url(r'^add_part',views.part_add_view,name='part_add'),
    url(r'^part_add_validate',views.part_add_validate,name='part_add_validate'),
    url(r'^details/(?P<pk>\w+)/$',views.part_details,name='part_details'),
    url(r'^search/$', views.part_search, name='part_search'),
    url(r'^form_fill/',views.form_fill,name='form_fill'),
    url(r'^stock_edit/',views.stock_edit,name='stock_edit'),
    url(r'^app_save/',views.app_save,name='app_save')
    # url(r'^part_stock_add_validate/(?P<pk>\w+)/$',views.part_stock_add_validate,name='part_stock_add_validate'),
]