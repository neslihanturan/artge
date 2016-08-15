# -*- coding: utf-8 -*-
from django import forms
from .models import SubMenuItem

class ContentForm(forms.ModelForm):

    class Meta:
        model = SubMenuItem
        fields = ('Alt menü Adı', 'İçerik',)
