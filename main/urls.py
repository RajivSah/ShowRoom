from django.conf.urls import url
from . import views

app_name='main'
urlpatterns = [
    url(r'^$',views.login_validate,name='login_page'),
    url(r'^logout/$', views.logout, name='logout'),
    #url(r'^validate$',views.login_validate,name='login_validate'),
    
]
