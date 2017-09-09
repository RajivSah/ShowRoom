from django.conf.urls import url
from . import views

app_name='main'
urlpatterns = [
    url(r'^$',views.login_validate,name='login_page'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^employee_list/$',views.list_employee.as_view(),name='employee_list'),
    url(r'^employee_detail/(?P<pk>\d+)/$',views.deail_employee.as_view(),name='employee_detail'),
    url(r'^employee_add/$',views.add_employee.as_view(),name='employee_add'),
    url(r'^employee_update/(?P<pk>\d+)$',views.update_employee.as_view(),name='employee_update'),
    url(r'^employee_search/',views.search_employee.as_view(),name='employee_search'),
    
]
