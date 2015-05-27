# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.template.defaultfilters import floatformat
from django import template

register = template.Library()

@register.filter
def float_format_v2(text, arg=-1):
    if int(text) == 0:
        return "-"
    else:
        return floatformat(text, arg)