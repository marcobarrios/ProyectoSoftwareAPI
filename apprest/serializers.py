from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Contacto, Telefono, TipoTelefono, ListaContacto, Evento

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email',)
        write_only_fields = ('password ',)


class ListaContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaContacto
        fields = ('id','usuario', 'nombreLista',)


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ('id', 'usuario', 'nombre', 'apellido', 'correo', 'fechaNacimiento', 'imagen', 'web','listaContacto',)


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
        fields = ('id', 'nombre', 'ubicacion', 'fechaInicio', 'fechaFin', 'todoDia','usuario',)
#        read_only_fields = ('usuario',)





