"""book_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. 'dd a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
l   1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from book_proj.index import view
from book_proj.book_view import bk_view
from book_proj.search import search_req
from book_proj.views import contact
from book_proj.book_order import add_cart
from  django.conf  import settings
from django.conf.urls.static import static
urlpatterns = [
    	url(r'^admin/', admin.site.urls),
    	url(r'^$', view),
	url(r'^search/$', search_req),
	url(r'^book/$', bk_view),
	url(r'^contact/$', contact),
	url(r'^cart/$', add_cart), 
	url(r'^contact-submit/$', add_cart),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
