#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from dictionary.models import *
from collections import defaultdict
import re

LAST_QUERIES = []


def index(request):
    return render_to_response('index.html', {'queries': LAST_QUERIES})


def grouping(data):
    d = defaultdict(list)
    for i in data:
        d[i.token1.lang].append(i)
    return dict(d)


def regex_filter(data, word):
    reg = re.compile(ur'\b{}\b'.format(word), flags=re.U)
    data = [i for i in data if reg.search(i.text) is not None]
    return data


def search(request):
    word = request.GET['q']
    if len(word) == 0:
        trans = []
    else:
        # print(ur'\b{}\b'.format(word))
        token = Token.objects.filter(text__contains=word)[:998]
        token = regex_filter(token, word)
        trans = Translation.objects.filter(token1__in=token)
        if word not in LAST_QUERIES:
            if len(LAST_QUERIES) >9:
                LAST_QUERIES.pop()
            LAST_QUERIES.insert(0, word)
    return render_to_response('results.html', {'word': word, 'trans': grouping(trans), 'empty': len(trans) == 0,
                                               'queries': LAST_QUERIES, 'langs':LANGS})
