# -*- coding: utf-8 -*-
from django.db import models


class SliderItem(models.Model):
    slider_item_title = models.CharField(max_length=15, verbose_name = 'Kayan Menü Sloganı')
    slider_item_explanation = models.CharField(max_length=50, verbose_name = 'Kayan Menü Açıklaması')

    def publish(self):
        self.save()
    def __str__(self):
        return self.slider_item_title


class ContactInformation(models.Model):
    phone = models.CharField(max_length=15, verbose_name = 'Telefon')
    email = models.CharField(max_length=15, verbose_name = 'E-posta')
    fax = models.CharField(max_length=15, verbose_name = 'Fax')
    address = models.CharField(max_length=50, verbose_name = 'Adres Bilgisi')

    class Meta:
        verbose_name = 'İletişim Bilgisi'

    def publish(self):
        self.save()
    def __str__(self):
        return self.address

class ReferenceItem(models.Model):
    reference_title = models.CharField(max_length=15, verbose_name = 'Referans Başlığı')
    reference_explanation = models.CharField(max_length=50, verbose_name = 'Referans Açıklaması')

    class Meta:
        verbose_name = 'Referans'
        verbose_name_plural = 'Referanslar'

    def publish(self):
        self.save()
    def __str__(self):
        return self.reference_title

class MenuItem(models.Model):
    item_name = models.CharField(max_length=15, verbose_name = 'Menü Adı')
    #metin = models.CharField(max_length=15, verbose_name = 'Menü Adı')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Menü Elemanı'
        verbose_name_plural = 'Menü Elemanları'

    def publish(self):
        self.save()
    def __str__(self):
        return self.item_name



class SubMenuItem(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='smenus')
    smenu_item_name = models.CharField(max_length=20, verbose_name = 'Alt Menü Adı')
    smenu_item_title = models.CharField(max_length=20, verbose_name = 'Metin Başlığı')
    metin = models.CharField(max_length=2000)

    #İf the title contains 'Prosil Nedir' then our page has special html file
    is_different_page = models.BooleanField(default=False)

    #smenu_item_content = models.CharField(max_length=20, verbose_name = 'İçerik')
    show_change_link = True
    class Meta:
        verbose_name = 'Alt Menü Elemanı'
        verbose_name_plural = 'Alt Menü Elemanları'
