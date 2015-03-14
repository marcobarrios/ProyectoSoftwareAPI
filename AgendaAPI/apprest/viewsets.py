from .models import Contacto, Telefono, TipoTelefono
from .serializers import ContactoSerializer, TelefonoSerializer, TipoTelefonoSerializer
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