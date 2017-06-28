from django.conf.urls import url
from . import views

app_name='main'
urlpatterns = [
    url(r'^(?P<login_status>[0,1])/$',views.login_page,name='login_page'),
    url(r'^validate$',views.login_validate,name='login_validate'),

]