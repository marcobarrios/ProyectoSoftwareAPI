# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0009_auto_20150410_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telefono',
            name='tipoTelefono',
        ),
    ]
