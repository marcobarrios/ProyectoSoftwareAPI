# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0002_auto_20150313_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=20)),
                ('imagen', models.ImageField(null=True, upload_to=b'Usuario')),
                ('correo', models.URLField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='fechaIncio',
            new_name='fechaInicio',
        ),
    ]
