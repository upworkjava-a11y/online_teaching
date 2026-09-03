from django import template
from django.utils.safestring import mark_safe

from apps.core.i18n.service import localize, localize_html, t

register = template.Library()


@register.filter(name="loc")
def loc(value):
    return localize(value)


@register.filter(name="loc_html")
def loc_html(value, slug=None):
    return mark_safe(localize_html(value, slug=slug))


@register.simple_tag
def trans_ui(message):
    return t(message)
