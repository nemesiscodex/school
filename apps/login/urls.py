from django.conf.urls import url
from django.urls import include, path
import apps.login.views as views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^auth', views.do_login),
]
