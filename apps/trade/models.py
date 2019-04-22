from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Goods
from datetime import datetime
# Create your models here.

User = get_user_model()


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0, verbose_name="购买数量")
    add_time = models.DateField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.goods_num)


class OrderInfo(models.Model):
    WAY = (
        (1, "自提"), (2, "堂食"), (3, "外送")
    )
    ORDER_STATUS = (
        ("success", "成功"), ("cancel", "取消"), ("cancel", "待支付")
    )
    PAY_TYPE = (
        ("alipay", '支付宝"'), ("wechat", "微信支付")
    )
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    order_sn = models.CharField(max_length=30, verbose_name="订单编号")
    trade_no = models.CharField(max_length=50, null=True, blank=True, unique=True, verbose_name="用户订单号")
    pay_status = models.CharField(choices=ORDER_STATUS, max_length=10, verbose_name="支付状态")
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
    post_script = models.TextField(max_length=200,  null=True, blank=True, verbose_name="用户留言")
    pay_time = models.DateField(null=True, blank=True, verbose_name="支付时间")
    add_time = models.DateField(default=datetime.now(), verbose_name="添加时间")
    get_way = models.IntegerField(default=1, null=True, blank=True, verbose_name="配送方式")
    get_time = models.DateField(null=True, blank=True, verbose_name="确认时间")

    address = models.CharField(max_length=500, default="", verbose_name="签收地址")
    signer_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="签收人姓名")
    signer_identity = models.CharField(max_length=9, verbose_name="签收人身份")
    signer_mobile = models.CharField(max_length=11, verbose_name="签收电话")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    order = models.ForeignKey(OrderInfo, verbose_name="订单", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0,verbose_name="商品数量")
    add_time = models.DateField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.order_sn
