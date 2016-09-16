# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160820_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submenuitem',
            name='smenu_item_content',
        ),
        migrations.AddField(
            model_name='submenuitem',
            name='smenu_item_title',
            field=models.CharField(verbose_name='Metin Başlığı', default='baslik', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submenuitem',
            name='menu_item',
            field=models.ForeignKey(to='app.MenuItem', related_name='smenus'),
        ),
    ]
