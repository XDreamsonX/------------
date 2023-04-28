from django.shortcuts import render
from .models import MenuItem

def menu(request, menu_name):
    menu_items = MenuItem.objects.filter(menu=menu_name, parent=None).order_by('order')
    return render(request, 'menu.html', {'menu_items': menu_items})