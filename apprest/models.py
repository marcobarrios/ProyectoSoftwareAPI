from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ListaContacto(models.Model):
    usuario = models.ForeignKey(User)
    nombreLista = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombreLista


class Contacto(models.Model):
    LISTA_CONTACTO = (
        ('1', 'Familia'),
        ('2', 'Amigos'),
        ('3', 'Trabajo'),
    )

    usuario = models.ForeignKey(User)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, null=True)
    correo = models.EmailField(null=True)
    fechaNacimiento = models.DateField(null=True)
    imagen = models.ImageField(upload_to="contacto", null=True)
    web = models.URLField(null=True)
    listaContacto = models.CharField(max_length=1, choices=LISTA_CONTACTO)



    def __unicode__(self):
        return self.nombre


class TipoTelefono(models.Model):
    tipoTelefono = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tipoTelefono


class Telefono(models.Model):
    TIPO_TELEFONO = (
        ('1', 'Celular'),
        ('2', 'Casa'),
        ('3', 'Trabajo'),
    )


    telefono = models.TextField()
    contacto = models.ForeignKey(Contacto)
    tipoTelefono = models.CharField(max_length=1, choices=TIPO_TELEFONO)

    def __unicode__(self):
        return self.telefono


class Evento(models.Model):
    usuario = models.ForeignKey(User)
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(null=True)
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField(null=True)
    todoDia = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nombre
