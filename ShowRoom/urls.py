from django.conf.urls import url,include
from django.contrib import admin
from main.views import home_page, login_validate


urlpatterns = [
    url(r'^admin/', admin.site.urls,name="admin"),
    url(r'^employee/', include('employee.urls')),
    url(r'^parts/',include('parts.urls')),
    url(r'^',include('main.urls')),

]
