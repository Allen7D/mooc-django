from django.db import models

from core.models import BaseModel
from apps.user.models import User


class City(models.Model):
    """城市"""
    name = models.CharField(verbose_name='城市', max_length=20)
    desc = models.CharField(verbose_name='描述', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = '城市列表'
        verbose_name_plural = verbose_name
        db_table = 'city'

    def __str__(self):
        return self.name


class Org(BaseModel):
    """课程机构"""
    name = models.CharField(verbose_name='机构名', max_length=50)
    image = models.ImageField(verbose_name='封面图', upload_to='org/%Y/%m', null=True, blank=True)
    desc = models.TextField(verbose_name='描述')
    tag = models.CharField(verbose_name='标签', max_length=10, default='全国知名')
    category = models.CharField(verbose_name='类别', max_length=4,
                                choices=(('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')),
                                default='pxjg')

    city = models.ForeignKey(City, verbose_name='所在城市', on_delete=models.DO_NOTHING)
    address = models.CharField(verbose_name='地址', max_length=150)
    # 布尔数据
    is_auth = models.BooleanField(verbose_name='是否认证', default=False)
    is_gold = models.BooleanField(verbose_name='是否金牌', default=False)
    # 动态数据
    course_nums = models.IntegerField(verbose_name='课程数', default=0)
    student_nums = models.IntegerField(verbose_name='学习人数', default=0)
    favor_nums = models.IntegerField(verbose_name='收藏数', default=0)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name
        db_table = 'org'

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    """机构教师"""
    user = models.OneToOneField(User, verbose_name='用户', on_delete=models.SET_NULL, null=True, blank=True)
    org = models.ForeignKey(Org, verbose_name='所属机构', on_delete=models.CASCADE)

    name = models.CharField(verbose_name='教师名', max_length=50)
    image = models.ImageField(verbose_name='头像', upload_to='teacher/%Y/%m', null=True, blank=True)
    age = models.IntegerField(verbose_name='年龄', default=18)
    work_years = models.IntegerField(verbose_name='工作年限', default=0)
    work_company = models.CharField(verbose_name='就职公司', max_length=50)
    work_position = models.CharField(verbose_name='公司职位', max_length=50)
    feature = models.CharField(verbose_name='教学特点', max_length=200)
    # 动态数据
    favor_nums = models.IntegerField(verbose_name='收藏数', default=0)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)

    class Meta:
        verbose_name = '机构教师'
        verbose_name_plural = verbose_name
        db_table = 'teacher'

    def __str__(self):
        return self.name
