# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0006_listacontacto_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallelistacontacto',
            name='contacto',
        ),
        migrations.RemoveField(
            model_name='detallelistacontacto',
            name='listaContacto',
        ),
        migrations.DeleteModel(
            name='DetalleListaContacto',
        ),
        migrations.AddField(
            model_name='contacto',
            name='listaContacto',
            field=models.ManyToManyField(to='apprest.ListaContacto'),
            preserve_default=True,
        ),
    ]
