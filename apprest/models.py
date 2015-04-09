from django.db import models

# Create your models here.

class Usuario(models.Model):    
    #owner = models.ForeignKey('auth.User', related_name='snippets')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    #imagen = models.ImageField(upload_to="Usuario",null=True)
    #fechaNacimiento = models.DateField(auto_now_add=True)
    #correo = models.URLField(null=True)
    def __unicode__(self):
        return self.nombre


class ListaContacto(models.Model):
    usuario = models.ForeignKey(Usuario)
    nombreLista = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombreLista


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, null=True)
    correo = models.EmailField(null=True)
    fechaNacimiento = models.DateField(null=True)
    imagen = models.ImageField(upload_to="contacto", null=True)
    web = models.URLField(null=True)
    listaContacto = models.ManyToManyField(ListaContacto)

    def __unicode__(self):
        return self.nombre


class TipoTelefono(models.Model):
    tipoTelefono = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tipoTelefono


class Telefono(models.Model):
    telefono = models.TextField()
    contacto = models.ForeignKey(Contacto)
    tipoTelefono = models.ForeignKey(TipoTelefono)

    def __unicode__(self):
        return self.telefono


class Evento(models.Model):
    usuario = models.ForeignKey(Usuario)
    nombre = models.TextField(max_length=100)
    ubicacion = models.TextField(max_length=100)
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    #todoDia = models.BooleanField()

    def __unicode__(self):
        return self.nombre
