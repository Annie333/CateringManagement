# Generated by Django 2.0 on 2019-04-28 11:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=0, verbose_name='商品数量')),
                ('add_time', models.DateField(default=datetime.datetime(2019, 4, 28, 11, 20, 37, 41204), verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sn', models.CharField(max_length=30, verbose_name='订单编号')),
                ('trade_no', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='用户订单号')),
                ('pay_status', models.CharField(choices=[('success', '成功'), ('cancel', '取消'), ('cancel', '待支付')], max_length=10, verbose_name='支付状态')),
                ('order_mount', models.FloatField(default=0.0, verbose_name='订单金额')),
                ('post_script', models.TextField(blank=True, max_length=200, null=True, verbose_name='用户留言')),
                ('pay_time', models.DateField(blank=True, null=True, verbose_name='支付时间')),
                ('add_time', models.DateField(default=datetime.datetime(2019, 4, 28, 11, 20, 37, 41204), verbose_name='添加时间')),
                ('get_way', models.IntegerField(blank=True, default=1, null=True, verbose_name='配送方式')),
                ('get_time', models.DateField(blank=True, null=True, verbose_name='确认时间')),
                ('address', models.CharField(default='', max_length=500, verbose_name='签收地址')),
                ('signer_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='签收人姓名')),
                ('signer_identity', models.CharField(max_length=9, verbose_name='签收人身份')),
                ('signer_mobile', models.CharField(max_length=11, verbose_name='签收电话')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=0, verbose_name='购买数量')),
                ('add_time', models.DateField(default=datetime.datetime(2019, 4, 28, 11, 20, 37, 41204), verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
    ]
