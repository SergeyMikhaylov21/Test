#!/usr/bin/python
#  -- coding: utf8 --

from django.db import models


LANGS = (('ru', u'русский'),
         ('en', u'английский'),
         ('fr', u'французский'),
         ('ge', u'немецкий'),
         ('it', u'итальянский'),
         ('es', u'испанский'))


class Token(models.Model):
    text = models.CharField(max_length=400, db_index=True)
    lang = models.CharField(max_length=3, choices=LANGS, db_index=True)


class Translation(models.Model):
    token1 = models.ForeignKey(Token, related_name='token1', db_index=True)
    token2 = models.ForeignKey(Token, related_name='token2', db_index=True)
    pos_token1 = models.CharField(max_length=20, blank=True, null=True)
    pos_token2 = models.CharField(max_length=20, blank=True, null=True)
    source = models.CharField(max_length=400)