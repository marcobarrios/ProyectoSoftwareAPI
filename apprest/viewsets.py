from django.contrib.auth.models import User
from .models import Contacto, Telefono, TipoTelefono, Evento, ListaContacto
from .serializers import ContactoSerializer, TelefonoSerializer, TipoTelefonoSerializer, EventoSerializer, ListaContactoSerializer , UserSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'


class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    lookup_field = 'id'


class ListaContactoViewSet(viewsets.ModelViewSet):
    serializer_class = ListaContactoSerializer
    queryset = ListaContacto.objects.all()
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        print request.user
        return super(ListaContactoViewSet,self).list(request,*args,**kwargs)



class ContactoViewSet(viewsets.ModelViewSet):
    serializer_class = ContactoSerializer
    queryset = Contacto.objects.all()
    lookup_field = 'id'


class TelefonoViewSet(viewsets.ModelViewSet):
    serializer_class = TelefonoSerializer
    queryset = Telefono.objects.all()
    lookup_field = 'id'


class TipoTelefonoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoTelefonoSerializer
    queryset = TipoTelefono.objects.all()
    lookup_field = 'id'






