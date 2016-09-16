# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_menuitem_metin'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='metin',
            field=models.CharField(max_length=15, verbose_name='Menü Adı', default='yok'),
            preserve_default=False,
        ),
    ]
