from django.db import models

from apps.org.models import Teacher
from core.models import BaseModel


class Course(BaseModel):
    name = models.CharField(verbose_name='课程名', max_length=50)
    teacher = models.ForeignKey(Teacher, verbose_name='讲师', on_delete=models.DO_NOTHING)
    desc = models.CharField(verbose_name='课程描述', max_length=300)
    learn_duration = models.IntegerField(verbose_name='学习时长(分钟)', default=0)
    degree = models.CharField(verbose_name='课程难度', max_length=2, choices=(('cj', '初级'), ('zj', '中极'), ('gj', '高级')))
    student_nums = models.IntegerField(verbose_name='学习人数', default=0)
    favor_nums = models.IntegerField(verbose_name='收藏数', default=0)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    category = models.CharField(verbose_name='课程分类', max_length=20, default='')
    tag = models.CharField(verbose_name='课程标签', max_length=10, default='')
    tips = models.CharField(verbose_name='课程须知', max_length=300, default='')
    overview = models.CharField(verbose_name='老师告诉你', max_length=300, default='')
    detail = models.TextField(verbose_name='课程详情')
    image = models.ImageField(verbose_name='封面图', upload_to='course/%Y/%m')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name
        db_table = 'course'

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    couser = models.ForeignKey(Course, on_delete=models.CASCADE)  # models.CASCADE表示 Course删除时情况关联的Lesson
    name = models.CharField(verbose_name='章节名', max_length=100)
    learn_duration = models.IntegerField(verbose_name='学习时长(分)', default=0)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name
        db_table = 'lesson'

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='视频名', max_length=100)
    learn_duration = models.IntegerField(verbose_name='学习时长(分)', default=0)
    url = models.CharField(verbose_name='访问地址', max_length=200)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name
        db_table = 'video'

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    '''课程资源'''
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='名称', max_length=100)
    file = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='资源地址')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
        db_table = 'course_resource'

    def __str__(self):
        return self.name