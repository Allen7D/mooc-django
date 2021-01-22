# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2021/1/22.
  Updated by Allen7D on 2021/1/22.
"""
from django.utils.safestring import mark_safe  # 用于导出

__author__ = 'Allen7D'


def django_mark(**kwargs):
    """搭配mark_safe使用，给新增的字段添加column_title"""

    def wrapper(f):
        for k, v in kwargs.items():
            setattr(f, k, v)
        return f

    return wrapper
