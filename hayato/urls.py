# -*- config: utf-8 -*-

from django.conf.urls import patterns, url
from hayato import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^world', views.world, name='world'),
    url(r'^news', views.news, name='news'),
)
