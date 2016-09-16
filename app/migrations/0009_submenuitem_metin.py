# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160830_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenuitem',
            name='metin',
            field=models.CharField(default='metin', max_length=20),
            preserve_default=False,
        ),
    ]
