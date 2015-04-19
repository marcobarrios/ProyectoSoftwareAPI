from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from apprest.viewsets import ContactoViewSet, TelefonoViewSet, TipoTelefonoViewSet, EventoViewSet, ListaContactoViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'usuarios', UserViewSet)
router.register(r'evento', EventoViewSet)
#router.register(r'listacontacto', ListaContactoViewSet)
router.register(r'contacto', ContactoViewSet)
router.register(r'telefono', TelefonoViewSet)
#router.register(r'tipotelefono', TipoTelefonoViewSet)





urlpatterns = patterns('',  # Examples:  # url(r'^$', 'test_rest.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^', include(router.urls)),
                       #url(r'^', include('apprest.urls')),
                       url(r'^token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       )
