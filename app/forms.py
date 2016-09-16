# -*- coding: utf-8 -*-
from django import forms
from redactor.widgets import RedactorEditor
from .models import SubMenuItem, ReferenceItem, MenuItem

class ContentForm(forms.ModelForm):
    # metin field is overridden in model form
    class Meta:
        model = SubMenuItem
        fields = ('smenu_item_name','smenu_item_title','metin','is_different_page')
        widgets = {
           'metin': RedactorEditor(),
           'is_different_page' : forms.HiddenInput()    #to hide is_different_page field
        }

class MenuForm(forms.ModelForm):
    metin = forms.CharField(required = False,widget=RedactorEditor(attrs={'readonly':'readonly'}))
    #metin = forms.CharField(required = False, label='Name of Institution')
    def __init__(self, *args, **kwargs):
        super(MenuForm,self).__init__(*args, **kwargs)
        print("from forms= title:",self.instance.item_name," id:",id(self.instance),", aktif mi:",self.instance.is_active)
        #self.instance.refresh_from_db()
        #fields = '__all__'
        #self.fields['metin'] = forms.CharField(required = True, label = "Card Holder Name",max_length = 60)
        #self.Meta.fields.append('metin')
        if not self.instance.is_active:
            if "metin" in self.fields:
                print('*******ife girdi')
                    #del self.fields['metin']
                self.fields['metin'].widget = forms.TextInput(attrs={'readonly':'readonly'},initial='http://')



        else:
            if "metin" in self.fields:
                print('*******else girdi')
                #self.fields['metin'] = forms.CharField()
                #self.fields['metin'].widget = RedactorEditor()


    class Meta:
        model = MenuItem

        fields = '__all__'



class ReferenceForm(forms.ModelForm):

    class Meta:
        model = ReferenceItem
        fields = ('reference_title','reference_explanation',)
        widgets = {
           'reference_explanation': forms.Textarea(attrs={'rows': 4, 'cols': 60}),
        }
