# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/18
@Author   : huanggangyu
"""

from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index2, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail')
]
