from django import template
register = template.Library()

@register.filter(name='add_commas')
def add_commas(value):
    return "{:,.0f}".format(value)