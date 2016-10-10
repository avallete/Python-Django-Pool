from django.conf.urls import url
from ex00 import views

urlpatterns = [
    url(r'^init/', views.init),
]
