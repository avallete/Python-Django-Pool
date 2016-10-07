from django.conf.urls import url
from ex02 import views

urlpatterns = [
    url(r'^$', views.main, name='ex02'),
    url(r'^post_new', views.post_new, name='post_new'),
]
