from django.conf.urls import url,include
from django.contrib import admin
from main.views import home_page, login_validate


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('main.urls')),
    url(r'^home/',include('home.urls')),
]
