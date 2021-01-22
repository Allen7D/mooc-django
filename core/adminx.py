# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2021/1/21.
  Updated by Allen7D on 2021/1/21.

  Font Awesome地址 https://fontawesome.dashgame.com/
"""

__author__ = 'Allen7D'


class BaseAdmin(object):
    list_display = []
    search_fields = []
    list_filter = []
    list_editable = []
    readonly_fields = ['create_time']  # 只读字段(无法修改)
    exclude = ['update_time', 'delete_time']  # 隐藏字段(不显示)

    def __add__(self, other):
        self.list_display = list(set(self.list_display + other.list_display))
        self.search_fields = list(set(self.search_fields + other.search_fields))
        self.list_filter = list(set(self.list_filter + other.list_filter))
        self.list_editable = list(set(self.list_editable + other.list_editable))
        self.list_editable = list(set(self.list_editable + other.list_editable))
        self.readonly_fields = list(set(self.readonly_fields + other.readonly_fields))
        self.exclude = list(set(self.exclude + other.exclude))

        return self
