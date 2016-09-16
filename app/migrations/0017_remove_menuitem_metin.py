# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_menuitem_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='metin',
        ),
    ]
