from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    nick_name = models.CharField(verbose_name='昵称', max_length=50, default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(verbose_name='性别', max_length=6, choices=(('male', '男'), ('female', '女')))
    address = models.CharField(verbose_name='地址', max_length=100, default='')
    mobile = models.CharField(verbose_name='手机号', max_length=11, unique=True)
    image = models.ImageField(verbose_name='头像', upload_to='avatar/%Y/%m', default='default.jpg')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        db_table = 'user'

    def __str__(self):
        return self.nick_name if self.nick_name else self.username