from django.conf.urls import url
from exos import views

urlpatterns = [
    url(r'^$', views.main),
]