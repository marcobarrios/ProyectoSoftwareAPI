from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Contacto, Telefono, TipoTelefono, ListaContacto, Evento
from passlib.handlers import md5_crypt



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email', 'username', 'password', )
        write_only_fields = ('password ',)

        def restore_object(self, attrs, instance=None):
            user = super(UserSerializer,self).restore_object(attrs, instance)
            hash = md5_crypt.encrypt(attrs['password'])
            user.set_password(hash)
            return user


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
        fields = ('id', 'nombre', 'ubicacion', 'fechaInicio', 'fechaFin', 'todoDia','usuario',)
#        read_only_fields = ('usuario',)





