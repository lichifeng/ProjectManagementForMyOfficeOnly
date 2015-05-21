# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django import template

register = template.Library()

@register.simple_tag
def icon(type, color="#000000"):
    return """<span class="glyphicon {0}" style="color: {1}" aria-hidden="true"></span>""".format(type, color)