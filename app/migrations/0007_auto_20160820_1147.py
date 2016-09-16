# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_submenuitem_smenu_item_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='item_name',
            field=models.CharField(verbose_name='Menü Adı', max_length=15),
        ),
        migrations.AlterField(
            model_name='submenuitem',
            name='smenu_item_content',
            field=models.CharField(verbose_name='İçerik', max_length=20),
        ),
        migrations.AlterField(
            model_name='submenuitem',
            name='smenu_item_name',
            field=models.CharField(verbose_name='Alt Menü Adı', max_length=20),
        ),
    ]
