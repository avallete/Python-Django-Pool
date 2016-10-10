from django.conf.urls import url
from ex03 import views

urlpatterns = [
    url(r'^populate/', views.populate),
    url(r'^display/', views.display),
]
