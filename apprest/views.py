from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from apprest.models import Contacto,DetalleListaContacto,ListaContacto, TipoTelefono, Telefono,Evento
from apprest.serializers import ContactoSerializer,DetalleListaContactoSerializer, ListaContactoSerializer, TipoTelefonoSerializer, TelefonoSerializer, EventoSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def contactos_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        contacto = Contacto.objects.all()
        serializer = ContactoSerializer(contacto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def listaContactos_list(request):
    if request.method == 'GET':
        lista = ListaContacto.objects.all()
        serializaer = ListaContactoSerializer(lista, many = True)
        return Response.serialize(serializaer.data)

    elif request.method == 'POST':
        serializaer = ListaContactoSerializer(data=request.data)
        if serializaer.is_valid():
            serializaer.save()
            return Response(serializaer.data,status=status.HTTP_201_CREATED)
        return Response(serializaer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Lista_detail_list(request):
    if request.method == 'GET':
        lista = DetalleListaContacto.object.all()
        serializer = DetalleListaContactoSerializer(lista, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DetalleListaContactoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response.serialize(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def tipo_telefono_list(request):
    if request.method == 'GET':
        tipos = TipoTelefono.objects.all()
        serializer = TipoTelefonoSerializer(tipos, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TipoTelefonoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status= status.HTTP_201_CREATED)
        return Response.serialize(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def telefono_list(request):
    if request.method == 'GET':
        telefono = Telefono.objects.all()
        serializer = TelefonoSerializer(telefono, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TelefonoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status= status.HTTP_201_CREATED)
        return Response.serialize(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def evento_list(request):
    if request.method == 'GET':
        telefono = Evento.objects.all()
        serializer = EventoSerializer(telefono, many = True)
        return Response(serializer.data)

    elif request.metheveod == 'POST':
        serializer = EventoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status= status.HTTP_201_CREATED)
        return Response.serialize(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
def lista_contacto_detail(request, pk):
    try:
        contactoD = ListaContacto.objects.get(pk=pk)
    except ListaContacto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = ListaContactoSerializer(contactoD)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ListaContactoSerializer(contactoD, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        contactoD.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT','DELETE'])
def contacto_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        contacto = Contacto.objects.get(pk=pk)
    except Contacto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactoSerializer(contacto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactoSerializer(contacto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contacto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def detallesLista_detail(request,pk):

    try:
        detalle = DetalleListaContacto.objects.get(pk = pk)
    except DetalleListaContacto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'GET':
        serializer = DetalleListaContactoSerializer(detalle)
        return  Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DetalleListaContactoSerializer(detalle, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif  request.method == 'DELETE':
        detalle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tipoTelefono_details(request, pk):
    try:
        tipo = TipoTelefono.objects.get(pk = pk)
    except TipoTelefono.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TipoTelefonoSerializer(tipo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TipoTelefonoSerializer(tipo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def Telefono_details(request, pk):
    try:
        telefono = Telefono.objects.get(pk = pk)
    except Telefono.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TelefonoSerializer(telefono)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TelefonoSerializer(telefono, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        telefono.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def Evento_details(request, pk):
    try:
        evento = Evento.objects.get(pk = pk)
    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventoSerializer(evento)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TelefonoSerializer(evento, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        evento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)