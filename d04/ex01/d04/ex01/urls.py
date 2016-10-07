from django.conf.urls import url
from ex01 import views

urlpatterns = [
    url(r'^django/', views.django, name='django'),
    url(r'^affichage/', views.affichage, name='affichange'),
    url(r'^templates/', views.templates, name='templates'),
]
