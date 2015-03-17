# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'contacto'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='apellido',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='correo',
            field=models.EmailField(max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='fechaNacimiento',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='web',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
