from .models import Contacto, Telefono, TipoTelefono, Usuario
from .serializers import ContactoSerializer, TelefonoSerializer, TipoTelefonoSerializer, UsuarioSerializer
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

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()