from django import template
from django.db.models import Q

from models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context.request.path
    menu_items = MenuItem.objects.filter(Q(parent=None) & Q(menu=menu_name))
    return generate_menu(menu_items, current_url)

def generate_menu(menu_items, current_url):
    menu = '<ul>'
    for item in menu_items:
        active_class = 'active' if current_url == item.url else ''
        menu += '<li class="' + active_class + '">'
        menu += '<a href="' + item.url + '">' + item.name + '</a>'
        children = MenuItem.objects.filter(Q(parent=item))
        if children:
            menu += generate_menu(children, current_url)
        menu += '</li>'
    menu += '</ul>'
    return menu