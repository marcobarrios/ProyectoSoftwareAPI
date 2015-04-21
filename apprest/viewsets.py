from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Contacto, Telefono, TipoTelefono, Evento, ListaContacto
from .serializers import ContactoSerializer, TelefonoSerializer, TipoTelefonoSerializer, EventoSerializer, ListaContactoSerializer , UserSerializer
from rest_framework import viewsets
from .permissions import IsStaffOrTargetUser
from passlib.handlers import md5_crypt


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

    def post_save(self, obj, created=False):
        hash = md5_crypt.encrypt(obj.password)
        if created:
            obj.set_password(hash)
            obj.save()

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'else IsStaffOrTargetUser()),


class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset.filter(usuario = self.request.user)
        return queryset



class ContactoViewSet(viewsets.ModelViewSet):
    serializer_class = ContactoSerializer
    queryset = Contacto.objects.all()
    lookup_field = 'id'

    def perform_create(self, serialised):
        serialised.save(usuario=self.request.user)

    #def create(self, request, *args, **kwargs):
    #   serialized = self.serializer_class(data=request.DATA)
#
#       if serialized.is_valid():
#           obj = serialized.usu
#           obj.usuario = request.user
#           self.pre_save(obj)
#           obj = serializer.save(force_insert=True)
#           self.post_save(obj, created=True)
#           headers = self.get_success_headers(serializer.data)
#           return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def get_queryset(self):
        query = self.request.QUERY_PARAMS
        queryset = self.queryset.filter(usuario = self.request.user)
        if 'lista' in query.keys():
            queryset = queryset.filter( listaContacto = query.get('lista'))
        return queryset

class TelefonoViewSet(viewsets.ModelViewSet):
    serializer_class = TelefonoSerializer
    queryset = Telefono.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        query = self.request.QUERY_PARAMS
        queryset = self.queryset
        if 'id' in query.keys():
            queryset = queryset.filter( contacto = Contacto.objects.get(id =query.get('id')))
        if 'tipo_telefono' in query.keys():
            queryset = queryset.filter( tipoTelefono = query.get('tipo_telefono'))
        return queryset


class ListaContactoViewSet(viewsets.ModelViewSet):
    serializer_class = ListaContactoSerializer
    queryset = ListaContacto.objects.all()
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        return super(ListaContactoViewSet,self).list(request,*args,**kwargs)

    def get_queryset(self):
        queryset = self.queryset.filter(usuario = self.request.user)
        return queryset


class TipoTelefonoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoTelefonoSerializer
    queryset = TipoTelefono.objects.all()
    lookup_field = 'id'






