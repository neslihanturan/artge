# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submenu_Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('smenu_item_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='menu_item',
            name='smenu_items',
            field=models.ManyToManyField(to='app.Submenu_Item'),
        ),
    ]
