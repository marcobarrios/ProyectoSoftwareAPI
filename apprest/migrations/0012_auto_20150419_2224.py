# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0011_telefono_tipotlefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telefono',
            name='tipoTlefono',
        ),
        migrations.AddField(
            model_name='telefono',
            name='tipoTelefono',
            field=models.CharField(default=1, max_length=1, choices=[(b'1', b'Celular'), (b'2', b'Casa'), (b'3', b'Trabajo')]),
            preserve_default=False,
        ),
    ]
