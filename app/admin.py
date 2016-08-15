# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import MenuItem, SubMenuItem

class SubMenuItemInline(admin.StackedInline):
    model = SubMenuItem
    extra = 0
    show_change_link = True

    verbose_name = "Alt Menü"
    verbose_name_plural = "Alt Menüler"


class MenuItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['item_name']}),
    ]
    inlines = [SubMenuItemInline]

class SubMenuAdmin(admin.ModelAdmin):
    #to hide submenu items on admin index
    def get_model_perms(self, request):
        return {}

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(SubMenuItem,SubMenuAdmin)
