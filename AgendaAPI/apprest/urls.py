from django.conf.urls import url
from apprest import views

urlpatterns = [
    url(r'^contacto/$', views.snippet_list),
    url(r'^contacto/(?P<pk>[0-9]+)/$', views.snippet_detail),
]