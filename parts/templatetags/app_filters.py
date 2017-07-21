from django import template

register = template.Library()

@register.filter(name='concatenate')
def concatenate(value,arg):
    return str(value)+str(arg)
