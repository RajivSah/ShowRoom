from .views import *
from django.conf.urls import url
from . import views


app_name ='vehicle_models'

urlpatterns = [
    url(r'^addImport/',AddModelImport.as_view(),name='addImport'),
    url(r'^processImport/',views.processImport,name='processImport'),

    url(r'^add_model/',AddManufacturer.as_view(),name='add_model'),
    url(r'^add_category/',AddVehicleCategories.as_view(),name='add_category'),
    url(r'^add_name/',AddVehicleName.as_view(),name='add_name'),
    #url(r'^add_vehicle/',views.addVehicle,name='add_vehicle'),
    url(r'^add_new_models/',AddModels.as_view(),name='add_new_models'),
    url(r'^add_model_details/',AddModelDetails.as_view(),name='add_model_details'),
    url(r'^update/(?P<pk>\d+)',UpdateManufacturer.as_view(),name='updateModel'),



]