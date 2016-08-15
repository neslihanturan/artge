# -*- coding: utf-8 -*-
from django.db import models


class MenuItem(models.Model):
    item_name = models.CharField(max_length=15, verbose_name = 'Menü Adı')

    class Meta:
        verbose_name = 'Menü Elemanı'
        verbose_name_plural = 'Menü Elemanları'

    def publish(self):
        self.save()
    def __str__(self):
        return self.item_name

class SubMenuItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    smenu_item_name = models.CharField(max_length=20, verbose_name = 'Alt Menü Adı')
    show_change_link = True
    class Meta:
        verbose_name = 'Alt Menü Elemanı'
        verbose_name_plural = 'Alt Menü Elemanları'

# Create your models here.
