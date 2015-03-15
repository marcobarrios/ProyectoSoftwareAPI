from .models import Contacto, Telefono, TipoTelefono, DetalleListaContacto, Evento
from .serializers import ContactoSerializer, TelefonoSerializer, TipoTelefonoSerializer, DetalleListaContactoSerializer, EventoSerializer
from rest_framework import viewsets
 
class ContactoViewSet(viewsets.ModelViewSet):
	serializer_class = ContactoSerializer
	queryset = Contacto.objects.all()
 
class TelefonoViewSet(viewsets.ModelViewSet):
	serializer_class = TelefonoSerializer
	queryset = Telefono.objects.all()

class TipoTelefonoViewSet(viewsets.ModelViewSet):
	serializer_class = TipoTelefonoSerializer
	queryset = TipoTelefono.objects.all()

class ListaContactosViewSet(viewsets.ModelViewSet):
    serializer_class = DetalleListaContactoSerializer
    queryset = DetalleListaContacto.objects.all()

class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
