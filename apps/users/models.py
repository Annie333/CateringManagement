from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    IDENTITY_KIND = (
        (1, "学生"), (2, "教师"), (3, "职工")
    )
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    sex = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(max_length=11,verbose_name="电话")
    mycode = models.CharField(max_length=15, null=True, blank=True, default="1234", verbose_name="密码")
    enter_date = models.DateField(null=True, blank=True, verbose_name="入学时间")
    identities = models.IntegerField(choices=IDENTITY_KIND, default=1, null=True, blank=True, verbose_name="身份")

    class Meta:
        verbose_name = "用户"
        #模型类的可读名称
        verbose_name_plural = "用户"

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    mycode = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")

    class Meta:
        verbose_name = "验证码"  # 模型类的可读名称
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.mycode

