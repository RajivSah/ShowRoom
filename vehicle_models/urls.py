from .views import *
from django.conf.urls import url

app_name ='vehicle_models'

urlpatterns = [
    url(r'^add_model/',add_model_first.as_view(),name='add_model'),
    url(r'^add_model_last/',add_model_last.as_view(),name='add_model_last'),
]