from django.conf.urls import url
from . import views

app_name='employee'
urlpatterns = [
    url(r'^$',views.home_page,name='home_page'),
]

