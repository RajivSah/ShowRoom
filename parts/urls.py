from django.conf.urls import url
from . import views

app_name='parts'
urlpatterns = [
    url(r'^$',views.parts_home,name='parts_home'),
    url(r'^add_part',views.part_add_view,name='part_add'),
    url(r'^part_add_validate',views.part_add_validate,name='part_add_validate'),
    url(r'^details/(?P<pk>[0-9 A-Z a-z]{1,30})/$',views.part_details,name='part_details'),
    url(r'^search/$', views.part_search, name='part_search'),

]