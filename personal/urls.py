from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^submit/',views.submit,name='submit'),
    url(r'^fourth/',views.fourth,name='fourth'),
    url(r'^work/',views.work,name='work'),
]