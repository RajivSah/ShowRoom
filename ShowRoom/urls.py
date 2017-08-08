from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls,name="admin"),
    url(r'^employee/', include('employee.urls')),
    url(r'^parts/',include('parts.urls')),
    url(r'^',include('main.urls')),
    url(r'^vehicle_models/', include('vehicle_models.urls')),
    url(r'^customer/',include('customer.urls')),
    url(r'^workshop/',include('workshop.urls')),

]
