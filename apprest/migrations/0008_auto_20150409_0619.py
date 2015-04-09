# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apprest', '0007_auto_20150409_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='usuario',
            field=models.ForeignKey(default=1, to='apprest.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='owner',
            field=models.ForeignKey(related_name='snippets', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
