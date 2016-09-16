# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20160903_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenuitem',
            name='is_different_page',
            field=models.BooleanField(default=False),
        ),
    ]
