# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0005_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='listacontacto',
            name='usuario',
            field=models.ForeignKey(default=1, to='apprest.Usuario'),
            preserve_default=False,
        ),
    ]
