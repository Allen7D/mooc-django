from django.contrib.auth import get_user_model
from django.db import models

from apps.course.models import Course
from core.models import BaseModel

User = get_user_model()


class UserAsk(models.Model):
    """用户咨询"""
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    mobile = models.CharField(max_length=11, verbose_name=u"手机")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name
        db_table = 'user_ask'

    def __str__(self):
        return '{name}_{course}({mobile})'.format(name=self.name, course=self.course_name, mobile=self.mobile)


class UserCourse(BaseModel):
    """用户课程"""
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name
        db_table = 'user_course'

    def __str__(self):
        return self.course.name


class CourseComment(BaseModel):
    """课程评论"""
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    comment = models.CharField(verbose_name='评论内容', max_length=200)

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name
        db_table = 'course_comment'

    def __str__(self):
        return self.comment


class UserFavor(BaseModel):
    """用户收藏"""
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    favor_id = models.IntegerField(verbose_name='收藏ID')
    favor_type = models.IntegerField(verbose_name='收藏类型', choices=((1, '课程'), (2, '机构'), (3, '讲师')), default=1)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        db_table = 'user_favor'

    def __str__(self):
        return '{user}_{id}'.format(user=self.user.username, id=self.favor_id)


class UserMessage(BaseModel):
    """用户消息"""
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='消息内容', max_length=200)
    has_read = models.BooleanField(verbose_name='是否已读', default=False)

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name
        db_table = 'user_message'

    def __str__(self):
        return self.content
