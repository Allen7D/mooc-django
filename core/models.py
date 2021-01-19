# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2021/1/18.
  Updated by Allen7D on 2021/1/18.
"""

from datetime import datetime

from django.db import models

__author__ = 'Allen7D'


class BaseModel(models.Model):
    create_time = models.DateField(verbose_name='创建时间', default=datetime.now)
    update_time = models.DateField(verbose_name='更新时间', default=datetime.now)
    delete_time = models.DateField(verbose_name='删除时间', default=datetime.now)

    class Meta:
        abstract = True

