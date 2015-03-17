from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
 
from apprest.viewsets import ContactoViewSet, TelefonoViewSet, TipoTelefonoViewSet, EventoViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'contacto', ContactoViewSet)
router.register(r'telefono', TelefonoViewSet)
router.register(r'tipotelefono', TipoTelefonoViewSet)
router.register(r'evento', EventoViewSet)
 
urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'test_rest.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	 
	url(r'^admin/', include(admin.site.urls)),
)
