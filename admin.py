from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent', 'order')
    list_filter = ('parent',)
    search_fields = ('name', 'url')

admin.site.register(MenuItem, MenuItemAdmin)