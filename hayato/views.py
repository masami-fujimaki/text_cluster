# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
import json

from database import Database
import mecab

def index(request):
    return render_to_response(
        'index.html',
        { 'categories': _categories(), },
        context_instance=RequestContext(request)
    )

def news(request):
    category = request.GET.get("category")
    dic_id = request.GET.get("dic_id")
    news_id = request.GET.get("news_id")
    db = Database()
    if dic_id:
        dic = db.dictionary(category, dic_id)
    if news_id:
        e =  db.news(news_id)
        news = { 
            'id': news_id,
            'text': _text(e['text'], dic['noun']), 
            'url': e['url'],
            'noun': mecab.get_news_noun(e['text']),
            }
        return HttpResponse(json.dumps(news))
    else:
        return HttpResponse(None)

def world(request):
    dic_id = request.GET.get("id")
    category = 'world'
    db = Database()
    dictionary = db.dictionary_category_words(category)
    if dic_id:
        news = db.dictionary_category_news(category, dic_id)
    else:
        news = {}
        
    return render_to_response(
        'dictionary.html',
        { 
            'category': category,
            'dictionary': dictionary,
            'news': news,
            'dic_id': dic_id,
        },
        context_instance=RequestContext(request)
    )


def _categories() :
    return ["economy","politics","world","sports","entertainments","life"];

def _text(text, noun):
    return text.replace(noun, "{{"+noun+"}}")    
