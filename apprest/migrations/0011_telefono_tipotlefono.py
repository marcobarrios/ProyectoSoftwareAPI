# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0010_remove_telefono_tipotelefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefono',
            name='tipoTlefono',
            field=models.CharField(default=1, max_length=7, choices=[(b'cel', b'Celular'), (b'casa', b'Casa'), (b'trabajo', b'Trabajo')]),
            preserve_default=False,
        ),
    ]
