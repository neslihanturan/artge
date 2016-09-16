# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160901_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefon')),
                ('email', models.CharField(max_length=15, verbose_name='E-posta')),
                ('fax', models.CharField(max_length=15, verbose_name='Fax')),
                ('address', models.CharField(max_length=15, verbose_name='Adres Bilgisi')),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('reference_title', models.CharField(max_length=15, verbose_name='Referans Başlığı')),
                ('reference_explanation', models.CharField(max_length=15, verbose_name='Referans Açıklaması')),
            ],
        ),
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('slider_item_title', models.CharField(max_length=15, verbose_name='Kayan Menü Sloganı')),
                ('slider_item_explanation', models.CharField(max_length=15, verbose_name='Kayan Menü Açıklaması')),
            ],
        ),
    ]
