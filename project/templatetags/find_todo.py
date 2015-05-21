# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django import template

register = template.Library()

@register.filter
def find_todo(value):
    for note in value.note_set.all():
        if not note.done:
            return True
    return False