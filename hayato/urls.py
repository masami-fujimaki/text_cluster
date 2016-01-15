# -*- config: utf-8 -*-

from django.conf.urls import patterns, url
from hayato import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^category/(.*)/$', views.category, name='category'),
    url(r'^category/(.*)/(.*)$', views.category, name='category'),
    url(r'^news', views.news, name='news'),
)
