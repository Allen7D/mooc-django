# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2021/1/19.
  Updated by Allen7D on 2021/1/19.
"""
from django.urls import path
from . import views

__author__ = 'Allen7D'

urlpatterns = [
    path('', views.index, name='index'),
]