from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User

from apprest.models import Contacto, ListaContacto, TipoTelefono, Telefono, Evento, Usuario
from apprest.serializers import ContactoSerializer, ListaContactoSerializer, TipoTelefonoSerializer, TelefonoSerializer, EventoSerializer, UsuarioSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly 

# Create your views here.

class Usuario_list(APIView):
    serializer_class = UserSerializer
    def get(self, request, format=None):
        usuario = User.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class Usuario_details(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk=pk)
        serializer = UserSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk=pk)
        serializer = UserSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk=pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class contactos_list(APIView):
    def get(self, request, format=None):
        contacto = Contacto.objects.all()
        serializer = ContactoSerializer(contacto, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class listaContactos_list(APIView):
    def get(self, request, format=None):
        lista = ListaContacto.objects.all()
        serializer = ListaContactoSerializer(lista, many=True)
        return Response.serialize(serializer.data)

    def post(self, request, format=None):
        serializer = ListaContactoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class tipo_telefono_list(APIView):
    def get(self, request, format=None):
        tipos = TipoTelefono.objects.all()
        serializer = TipoTelefonoSerializer(tipos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TipoTelefonoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class telefono_list(APIView):
    def get(self, request, format=None):
        telefono = Telefono.objects.all()
        serializer = TelefonoSerializer(telefono, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TelefonoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class evento_list(APIView):
    def get(self, request, format=None):
        telefono = Evento.objects.all()
        serializer = EventoSerializer(telefono, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            ob = serializer.object
            ob.usuario = request.user
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class lista_contacto_detail(APIView):
    def get_object(self, pk):
        try:
            return ListaContacto.objects.get(pk=pk)
        except ListaContacto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        contactoD = self.get_object(pk)
        serializer = ListaContactoSerializer(contactoD)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contactoD = self.get_object(pk)
        serializer = ListaContactoSerializer(contactoD, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contactoD = self.get_object(pk)
        contactoD.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class contacto_detail(APIView):
    def get_object(self, pk):
        try:
            return Contacto.objects.get(pk=pk)
        except Contacto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        contacto = self.get_object(pk=pk)
        serializer = ContactoSerializer(contacto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contacto = self.get_object(pk=pk)
        serializer = ContactoSerializer(contacto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contacto = self.get_object(pk=pk)
        contacto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class tipoTelefono_details(APIView):
    def get_object(self, pk):
        try:
            return TipoTelefono.objects.get(pk = pk)
        except TipoTelefono.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tipo = self.get_object(pk=pk)
        serializer = TipoTelefonoSerializer(tipo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tipo = self.get_object(pk=pk)
        serializer = TipoTelefonoSerializer(tipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tipo = self.get_object(pk=pk)
        tipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Telefono_details(APIView):
    def get_object(self, pk):
        try:
            return Telefono.objects.get(pk=pk)
        except Telefono.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        telefono = self.get_object(pk=pk)
        serializer = TelefonoSerializer(telefono)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        telefono = self.get_object(pk=pk)
        serializer = TelefonoSerializer(telefono, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        telefono = self.get_object(pk=pk)
        telefono.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Evento_details(APIView):
    def get_object(self, pk):
        try:
            return Evento.objects.get(pk=pk)
        except Evento.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        evento = self.get_object(pk=pk)
        serializer = EventoSerializer(evento)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        evento = self.get_object(pk=pk)
        serializer = TelefonoSerializer(evento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        evento = self.get_object(pk=pk)
        evento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



