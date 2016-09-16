# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_contactinformation_referenceitem_slideritem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactinformation',
            options={'verbose_name': 'İletişim Bilgisi'},
        ),
        migrations.AlterModelOptions(
            name='referenceitem',
            options={'verbose_name': 'Referans', 'verbose_name_plural': 'Referanslar'},
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='address',
            field=models.CharField(verbose_name='Adres Bilgisi', max_length=50),
        ),
        migrations.AlterField(
            model_name='referenceitem',
            name='reference_explanation',
            field=models.CharField(verbose_name='Referans Açıklaması', max_length=50),
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='slider_item_explanation',
            field=models.CharField(verbose_name='Kayan Menü Açıklaması', max_length=50),
        ),
    ]
