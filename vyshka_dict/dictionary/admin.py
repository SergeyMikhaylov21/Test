#!/usr/bin/python3.4
#  -- coding: utf8 --

from django.contrib import admin

from dictionary.models import *


# class TokenAdmin(admin.ModelAdmin):
#     list_display = ('text', 'text_eng', 'text_rus', 'created')  # в таблице

admin.site.register(Token)
admin.site.register(Translation)