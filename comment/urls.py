# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/19
@Author   : huanggangyu
"""

from django.conf.urls import url
from . import views

app_name = 'comment'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment')
]
