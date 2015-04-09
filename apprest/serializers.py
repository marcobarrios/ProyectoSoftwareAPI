from rest_framework import serializers
from .models import Contacto, Telefono, TipoTelefono, ListaContacto, Evento , Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    #owner = serializers.Field('owner.username')
    class Meta:
        model  = Usuario
        #fields = ('nombre', 'apellido','owner',)
        fields = ('nombre', 'apellido',)

class ListaContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaContacto
        fields = ('id','usuario', 'nombreLista',)


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ('id', 'nombre', 'apellido', 'correo', 'fechaNacimiento', 'imagen', 'web','listaContacto',)


class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = ('id', 'telefono', 'contacto', 'tipoTelefono',)


class TipoTelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTelefono
        fields = ('id', 'tipoTelefono',)


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id', 'nombre', 'ubicacion', 'fechaInicio', 'fechaFin',)





