# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_menuitem_metin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submenuitem',
            old_name='menu_item',
            new_name='menuitem',
        ),
    ]
