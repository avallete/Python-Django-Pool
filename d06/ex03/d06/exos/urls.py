from django.conf.urls import url
from exos import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
]