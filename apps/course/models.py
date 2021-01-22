# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2021/1/20.
  Updated by Allen7D on 2021/1/20.
"""

from django.db import models

from DjangoUeditor.models import UEditorField
from apps.org.models import Teacher, Org
from core.models import BaseModel
from core.utils import django_mark, mark_safe

__author__ = 'Allen7D'


class Course(BaseModel):
    """课程"""
    name = models.CharField(verbose_name='课程名', max_length=50)
    org = models.ForeignKey(Org, verbose_name='机构', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name='讲师', on_delete=models.DO_NOTHING)
    desc = models.CharField(verbose_name='课程描述', max_length=300)
    learn_duration = models.IntegerField(verbose_name='学习时长(分钟)', default=0)
    degree = models.CharField(verbose_name='课程难度', max_length=2, choices=(('cj', '初级'), ('zj', '中极'), ('gj', '高级')))
    category = models.CharField(verbose_name='课程分类', max_length=20, default='')
    tag = models.CharField(verbose_name='课程标签', max_length=10, default='')
    tips = models.CharField(verbose_name='课程须知', max_length=300, default='')
    notice = models.CharField(verbose_name='课程公告', max_length=300, default='')
    overview = models.CharField(verbose_name='内容概览', max_length=300, default='')  # 老师告诉你
    # detail = models.TextField(verbose_name='课程详情')  # 改为UEditorField, 字段的类型不变
    detail = UEditorField(verbose_name='课程详情', width=600, height=300, imagePath='courses/ueditor/images/',
                          filePath='courses/ueditor/files/', default='')
    image = models.ImageField(verbose_name='封面图', upload_to='course/%Y/%m')
    is_classics = models.BooleanField(verbose_name='是否经典', default=False)
    is_banner = models.BooleanField(verbose_name='是否首页轮播', default=False)
    # 动态数据
    student_nums = models.IntegerField(verbose_name='学习人数', default=0)
    favor_nums = models.IntegerField(verbose_name='收藏数', default=0)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name
        db_table = 'course'

    def __str__(self):
        return self.name

    @django_mark(short_description='图片')
    def show_image(self):
        # image字段必须为非空
        column_title = "<img src='{}' width='200px'>".format(self.image.url)
        return mark_safe(column_title)

    @django_mark(short_description='跳转')
    def go_to(self):
        column_title = "<a href='/course/{}'>跳转</a>".format(self.id)
        return mark_safe(column_title)


# 用于首页Banner显示
class BannerCourse(Course):
    """轮播课程"""

    class Meta:
        verbose_name = '轮播课程'
        verbose_name_plural = verbose_name
        proxy = True


# 基于标签找同类课程
class CourseTag(BaseModel):
    """课程标签"""
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    tag = models.CharField(verbose_name='标签', max_length=10)

    class Meta:
        verbose_name = '课程标签'
        verbose_name_plural = verbose_name
        db_table = 'course_tag'

    def __str__(self):
        return self.tag


class Lesson(BaseModel):
    """章节"""
    course = models.ForeignKey(Course, verbose_name='课程',
                               on_delete=models.CASCADE)  # models.CASCADE表示 Course删除时情况关联的Lesson
    name = models.CharField(verbose_name='章节名', max_length=100)
    learn_duration = models.IntegerField(verbose_name='学习时长(分)', default=0)

    class Meta:
        verbose_name = '课程章节'
        verbose_name_plural = verbose_name
        db_table = 'lesson'

    def __str__(self):
        return self.name


class Video(BaseModel):
    """视频"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='视频名', max_length=100)
    learn_duration = models.IntegerField(verbose_name='学习时长(分)', default=0)
    url = models.CharField(verbose_name='访问地址', max_length=200)

    class Meta:
        verbose_name = '课程视频'
        verbose_name_plural = verbose_name
        db_table = 'video'

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    """课程资源"""
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='名称', max_length=100)
    file = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='资源地址', null=True, blank=True)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
        db_table = 'course_resource'

    def __str__(self):
        return self.name


class CourseTag(BaseModel):
    """课程标签"""
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    tag = models.CharField(verbose_name="标签", max_length=100)

    class Meta:
        verbose_name = "课程标签"
        verbose_name_plural = verbose_name
        db_table = 'course_tag'

    def __str__(self):
        return self.tag


class Banner(BaseModel):
    title = models.CharField(verbose_name='标题', max_length=100)
    image = models.ImageField(verbose_name='轮播图', max_length=200, upload_to='banner/%Y/%m')
    url = models.URLField(verbose_name='访问地址', max_length=200)
    index = models.IntegerField(verbose_name='顺序', default=0)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
        db_table = 'banner'

    def __str__(self):
        return self.title
