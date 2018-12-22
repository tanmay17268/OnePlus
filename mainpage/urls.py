from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
	url(r'^$', views.index,name="index"),
	url(r'^personal/',include('personal.urls')),
	url(r'^connect/',include('connect.urls')),
    url(r'^plusone/',include('plusone.urls')),
]