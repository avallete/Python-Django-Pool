from django.conf.urls import url
from ex00 import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.ex00),
]