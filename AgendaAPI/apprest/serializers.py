from rest_framework import serializers
from .models import Contacto, Telefono, TipoTelefono, ListaContacto, DetalleListaContacto, Evento, Usuario


class ListaContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaContacto
        fields = ('id', 'nombreLista',)

class ContactoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contacto
		fields = ('id', 'nombre', 'apellido', 'correo', 'fechaNacimiento', 'imagen', 'web',)

class DetalleListaContactoSerializer (serializers.ModelSerializer):
    class Meta:
        model = DetalleListaContacto
        fields = ('idListaContacto', 'idContacto',)

class TipoTelefonoSerializer(serializers.ModelSerializer):
	class Meta:
		model = TipoTelefono
		fields = ('id', 'tipoTelefono',)

class TelefonoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Telefono
		fields = ('id', 'telefono', 'contacto', 'tipoTelefono',)

class EventoSerializer( serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id', 'nombre', 'ubicacion', 'fechaInicio', 'fechaFin',)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Usuario
        fields = ('nombre', 'apellido', 'contrasenia', 'imagen', 'correo',)




