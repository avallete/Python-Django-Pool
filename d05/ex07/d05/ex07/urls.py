from django.conf.urls import url
from ex07 import views

urlpatterns = [
    url(r'^populate/', views.populate),
    url(r'^display/', views.display),
    url(r'^remove/', views.remove),
    url(r'^update/', views.update),
]
