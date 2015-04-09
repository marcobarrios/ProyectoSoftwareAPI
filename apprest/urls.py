from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from apprest import views

urlpatterns = [
    url(r'^usuarios/$', views.usuario_list.as_view()),
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.Usuario_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)