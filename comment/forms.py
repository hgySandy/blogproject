# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/19
@Author   : huanggangyu
"""

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
