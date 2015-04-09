from .models import Contacto, Telefono, TipoTelefono, DetalleListaContacto, Evento, ListaContacto , Usuario
from .serializers import ContactoSerializer, TelefonoSerializer, TipoTelefonoSerializer, DetalleListaContactoSerializer, \
    EventoSerializer, ListaContactoSerializer , UsuarioSerializer
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


class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()


class DetalleListaContactosViewSet(viewsets.ModelViewSet):
    serializer_class = DetalleListaContactoSerializer
    queryset = DetalleListaContacto.objects.all()


class ListaContactoViewSet(viewsets.ModelViewSet):
    serializer_class = ListaContactoSerializer
    queryset = ListaContacto.objects.all()

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()




