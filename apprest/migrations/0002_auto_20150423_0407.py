# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fechaFin',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
