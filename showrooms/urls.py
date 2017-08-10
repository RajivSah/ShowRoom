from django.conf.urls import url
from . import views
from vehicle_models.views import AddManufacturer

app_name='showrooms'

urlpatterns=[


    url(r'^add_model/', AddManufacturer.as_view(), name='add_model'),
    url(r'^newSale/', views.NewSaleView.as_view(), name='newSale'),
    url(r'^salesList/', views.ListSalesView.as_view(), name='salesList'),
    url(r'^$', views.ManufacturerListView.as_view(), name='manufacturerLists'),
    url(r'^manufacturer/category/(?P<pk>\d+)/$', views.CategoryListView.as_view(), name='categoryList'),
    url(r'^manufacturer/category/vehicleName/(?P<pk>\d+)/$', views.VehicleNameListView.as_view(), name='vehicleNameList'),
    url(r'^manufacturer/category/vehicleName/models/(?P<pk>\d+)/$', views.ModelListView.as_view(), name='modelList'),
    url(r'^manufacturer/category/vehicleName/models/details/(?P<pk>\d+)/$', views.ModelDetailsView.as_view(), name='modelDetails'),








]