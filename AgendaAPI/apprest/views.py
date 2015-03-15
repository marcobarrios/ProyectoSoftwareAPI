from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from apprest.models import Contacto,Usuario
from apprest.serializers import ContactoSerializer, UsuarioSerializer

# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def contactos_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        contacto = Contacto.objects.all()
        serializer = ContactoSerializer(contacto, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def contacto_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        contacto = Contacto.objects.get(pk=pk)
    except Contacto.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ContactoSerializer(contacto)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContactoSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        contacto.delete()
        return HttpResponse(status=204)

def usuarios(request,pk):

    try:
        usuario = Usuario.objects.get(pk = pk)
    except Usuario.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(snippet, data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        usuario.delete()
        return HttpResponse(status=204)

