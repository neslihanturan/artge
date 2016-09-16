# -*- coding: utf-8 -*-
from django.contrib import admin
from .forms import ContentForm, ReferenceForm, MenuForm
from .models import MenuItem, SubMenuItem, ContactInformation, ReferenceItem, SliderItem
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import TextInput, Textarea
from django.db import models



class SubMenuItemInline(admin.StackedInline):
    model = SubMenuItem
    extra = 0  #to add zero submenu default
    show_change_link = True  #link to edit details of submenu
    exclude = ('smenu_item_content','is_different_page','metin') # to hide içerik and is_different_page fields at upper menu
    class Meta:
        verbose_name = "Alt Menü"
        verbose_name_plural = "Alt Menüler"


        #if sender.menu_item.submenuitem_set.count() == 0:
        #    print('test3')


class MenuItemAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    (None,               {'fields': ['item_name']}),
    #]
    #readonly_fields=('item_name',)
    inlines = [SubMenuItemInline]
    list_display = ('item_name', 'get_sub_menus')
    form = MenuForm


    def get_sub_menus(self, obj):   #to list sub menu names
        names = ""
        for i in obj.smenus.all():  #iterate on related objects
            names += '{:^36} {} '.format(i.smenu_item_name,',')
        return names
    get_sub_menus.short_description = 'Alt Menüler'

    #def has_add_permission(self, request):
    #    return False


    def has_delete_permission(self, request, obj=None):
        return False



class SubMenuAdmin(admin.ModelAdmin):
    verbose_name = "Alt Menü Elemanı"
    verbose_name_plural = "Alt Menü Elemanları"

    form = ContentForm

    #to hide submenu items on admin first page
    def get_model_perms(self, request):
        return {}

    def save(self):
        #keys = ['Prosil','Nedir']
        #if any(x in self.cleaned_data['smenu_item_title'] for x in keys):
        #print(self.obj.smenus.item_name)

        print('test')
        if "Prosil Nedir" in self.cleaned_data['smenu_item_title']:
            is_different_page = True
        super(SubMenuAdmin, self).save()


    #def save(self, *args, **kwargs):
    #    print(self.obj.smenus.item_name)
    #    print('test')
    #    super(Model, self).save(*args, **kwargs)

    #to redirect to menu items change list after saving changes
    def response_change(self, request, obj):

        print(obj.menuitem.item_name)
        print('test')
        return HttpResponseRedirect(reverse("admin:app_menuitem_changelist"))


    def response_add(self, request, obj):
        print(obj.menuitem.item_name)
        print('test')
        return HttpResponseRedirect(reverse("admin:app_menuitem_changelist"))



class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address','fax','email')
    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        #Disable delete
        actions = super(ContactInformationAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

class ReferenceItemAdmin(admin.ModelAdmin):
    form = ReferenceForm
    list_display = ('reference_title','reference_explanation')


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(ReferenceItem, ReferenceItemAdmin)
admin.site.register(SubMenuItem,SubMenuAdmin)
