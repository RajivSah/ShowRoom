from django.conf.urls import url
from . import views

app_name='parts'
urlpatterns = [
    url(r'^$',views.parts_home,name='parts_home'),
]