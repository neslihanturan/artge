# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_submenuitem_metin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenuitem',
            name='metin',
            field=models.CharField(max_length=2000),
        ),
    ]
