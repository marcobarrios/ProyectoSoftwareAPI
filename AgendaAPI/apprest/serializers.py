from rest_framework import serializers
from .models import Contacto, Telefono, TipoTelefono
 
class ContactoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contacto
		fields = ('id', 'nombre', 'apellido', 'correo', 'fechaNacimiento', 'imagen', 'web',)
 
class TelefonoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Telefono
		fields = ('id', 'telefono', 'contacto', 'tipoTelefono',)

class TipoTelefonoSerializer(serializers.ModelSerializer):
	class Meta:
		model = TipoTelefono
		fields = ('id', 'tipoTelefono',)
