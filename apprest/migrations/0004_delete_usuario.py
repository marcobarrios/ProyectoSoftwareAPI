# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0003_auto_20150314_2327'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
