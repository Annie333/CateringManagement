from django.db import models
from goods.models import Windows
# Create your models here.


class Staff(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    sex = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    mycode = models.CharField(max_length=15, null=True, blank=True, default="1234", verbose_name="密码")
    enter_date = models.DateField(null=True, blank=True, verbose_name="入职时间")
    wid = models.ForeignKey(Windows, verbose_name="员工所在窗口", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


