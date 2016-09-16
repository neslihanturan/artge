# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_submenuitem_is_different_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='metin',
            field=models.CharField(max_length=15, default='none', verbose_name='Menü Adı'),
            preserve_default=False,
        ),
    ]
