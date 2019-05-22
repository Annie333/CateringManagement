from django.db import models
from django.contrib.auth import get_user_model
from trade.models import OrderInfo

from goods.models import Goods
from goods.models import Windows
from datetime import datetime
# Create your models here.
User = get_user_model()


class UserGoodsFav(models.Model):
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE, help_text="商品id")
    add_time = models.DateField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏商品"
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")#联合唯一，数据库内完成，若记录重复，数据库抛出异常

    def __str__(self):
        return self.user.username


class UserWindowsFav(models.Model):
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    windows = models.ForeignKey(Windows, verbose_name="窗口", on_delete=models.CASCADE)
    add_time = models.DateField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏窗口"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class LeavingMessage(models.Model):
    MESSAGE_CHOICE = (
        ("1", "留言"), ("2", "投诉"), ("3", "询问"), ("4", "售后"), ("5", "求购"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    windows = models.ForeignKey(Windows, on_delete=models.CASCADE, verbose_name="窗口")
    msg_type = models.CharField(max_length=2, choices=MESSAGE_CHOICE, default="1", help_text="留言类型1(留言),2(投诉),3,(询"
                                                                                             "问),4(售后),5(求购)",
                                verbose_name="留言类型")
    message = models.TextField(default="", verbose_name="留言内容", help_text="留言内容")
    file = models.FileField(verbose_name="上传文件", help_text="上传文件")
    subject = models.CharField(max_length=100, default="", verbose_name="主题")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    province = models.CharField(max_length=100, default="", verbose_name="省份")
    city = models.CharField(max_length=100, default="", verbose_name="城市")
    district = models.CharField(max_length=100, default="", verbose_name="区域")
    address = models.CharField(max_length=100, default="", verbose_name="地址")
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="签收电话")
    signer_name = models.CharField(max_length=100, default="", verbose_name="签收人")
    signer_identity = models.CharField(max_length=9, verbose_name="签收人身份")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "签收地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
