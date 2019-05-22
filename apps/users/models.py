from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from goods.models import Windows
# Create your models here.


class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    sex = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(max_length=11, verbose_name="电话", unique=True, null=True, blank=True)
    identities = models.CharField(max_length=9, null=True, blank=True, verbose_name="身份号码")
    enter_date = models.DateField(null=True, blank=True, verbose_name="入学时间")

    class Meta:
        verbose_name = "用户"
        #模型类的可读名称
        verbose_name_plural = "用户"

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    code = models.CharField(max_length=10, verbose_name="验证码", default="")
    mobile = models.CharField(max_length=11, verbose_name="电话")

    class Meta:
        verbose_name = "验证码"  # 模型类的可读名称
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.code


class Staff(models.Model):
    user = models.OneToOneField(UserProfile,verbose_name="用户", on_delete=models.CASCADE)
    windows = models.ForeignKey(Windows, related_name='windows', null=True, verbose_name="员工所在窗口",
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = "员工"
        # 模型类的可读名称
        verbose_name_plural = "员工"

    def __str__(self):
        return self.user.username
