from django.db import models
from core.models import BaseModel


class City(models.Model):
    '''城市'''
    name = models.CharField(verbose_name='城市', max_length=20)
    desc = models.CharField(verbose_name='描述', max_length=200)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name
        db_table = 'city'

    def __str__(self):
        return self.name


class Org(BaseModel):
    '''课程机构'''
    name = models.CharField(verbose_name='机构名', max_length=50)
    desc = models.TextField(verbose_name='描述')
    tag = models.CharField(verbose_name='标签', max_length=10, default='全国知名')
    category = models.CharField(verbose_name='类别', max_length=4, choices=(('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')),
                                default='pxjg')
    course_nums = models.IntegerField(verbose_name='课程数', default=0)
    student_nums = models.IntegerField(verbose_name='学习人数', default=0)
    favor_nums = models.IntegerField(verbose_name='收藏数', default=0)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    city = models.ForeignKey(City, verbose_name='所在城市', on_delete=models.DO_NOTHING)
    address = models.CharField(verbose_name='地址', max_length=150)
    image = models.ImageField(verbose_name='封面图', upload_to='org/%Y/%m')

    class Meta:
        verbose_name = '机构'
        verbose_name_plural = verbose_name
        db_table = 'org'

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    '''机构教师'''
    org = models.ForeignKey(Org, verbose_name='所属机构', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='机构名', max_length=50)
    age = models.IntegerField(verbose_name='', default=18)
    work_years = models.IntegerField(verbose_name='', default=0)
    work_company = models.CharField(verbose_name='', max_length=50)
    work_position = models.CharField(verbose_name='', max_length=50)
    feature = models.CharField(verbose_name='', max_length=50)
    favor_nums = models.IntegerField(verbose_name='收藏数', default=0)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    image = models.ImageField(verbose_name='', upload_to='teacher/%Y/%m')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name
        db_table = 'teacher'

    def __str__(self):
        return self.name
