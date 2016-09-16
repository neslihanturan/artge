from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from app.forms import MenuForm
from django import forms
from app.models import *
from django.core.exceptions import ObjectDoesNotExist
#from django.db.models.base import ObjectDoesNotExist

@receiver(post_save, sender=SubMenuItem)
def sub_menu_post_save(sender, **kwargs):
    try:
        instance = kwargs.get('instance', None)
        if instance.menuitem.smenus.count() == 1: # first sub menu created
            print('ilkini olusturdun')
            MenuItem.objects.filter(pk=instance.menuitem.pk).update(is_active = False)  #if dont update db, only this instance will be updated
            instance.menuitem.refresh_from_db() #to make all instances syncronised
            print("from signals= title:",instance.menuitem.item_name," id:",id(instance.menuitem),", aktif mi:",instance.menuitem.is_active)
            ##delete code here
            ###MenuForm.remove_field(instance.menuitem.form)
        print("2. message",instance.menuitem.smenus.count())
    except (MenuItem.DoesNotExist, ObjectDoesNotExist) as e:
        print('error2')


@receiver(pre_delete, sender=SubMenuItem)
def sub_menu_pre_delete(sender, **kwargs):
    print("deleting")
    try:
        instance = kwargs.get('instance', None)
        if instance.menuitem.smenus.count() == 1: # last remained sub menu will be deleted soon
            print('hepsini sildin')
            MenuItem.objects.filter(pk=instance.menuitem.pk).update(is_active = True)  #if dont update db, only this instance will be updated
            instance.menuitem.refresh_from_db() #to make all instances syncronised
        print("1. message",instance.menuitem.smenus.count())
    except (MenuItem.DoesNotExist, ObjectDoesNotExist) as e:
        print('error1')

post_save.connect(sub_menu_post_save, sender=SubMenuItem, dispatch_uid="sub_menu_post_save")
pre_delete.connect(sub_menu_pre_delete, sender=SubMenuItem, dispatch_uid="sub_menu_pre_delete")
