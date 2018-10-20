# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/18
@Author   : huanggangyu
"""
from __future__ import unicode_literals

try:
    from settings.settings_local import *
except ImportError as ie:
    print("请在settings目录下添加settings_local.py文件，内容可参照settings_local.py.template")
except Exception as e:
    print("严重错误")
    print(e)
