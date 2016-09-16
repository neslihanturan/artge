# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20160905_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
