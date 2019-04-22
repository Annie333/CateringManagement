# Generated by Django 2.2 on 2019-04-17 12:03

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
            name='LeavingMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesg_type', models.CharField(choices=[(1, '留言'), (2, '投诉'), (3, '询问'), (4, '售后'), (5, '求购')], default=1, help_text='留言类型1(留言),2(投诉),3,(询问),4(售后),5(求购)', max_length=1, verbose_name='留言类型')),
                ('message', models.TextField(default='', help_text='留言内容', verbose_name='留言内容')),
                ('file', models.FileField(help_text='上传文件', upload_to='', verbose_name='上传文件')),
                ('subject', models.CharField(default='', max_length=100, verbose_name='主题')),
                ('add_time', models.DateField(default=datetime.datetime(2019, 4, 17, 20, 3, 41, 319059), verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户留言',
                'verbose_name_plural': '用户留言',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(default='', max_length=100, verbose_name='区域')),
                ('address', models.CharField(default='', max_length=100, verbose_name='地址')),
                ('signer_mobile', models.CharField(default='', max_length=11, verbose_name='签收电话')),
                ('signer_name', models.CharField(default='', max_length=100, verbose_name='签收人')),
                ('add_time', models.DateField(default=datetime.datetime(2019, 4, 17, 20, 3, 41, 335082), verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '签收地址',
                'verbose_name_plural': '签收地址',
            },
        ),
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(default=datetime.datetime(2019, 4, 17, 20, 3, 41, 319059), verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
            },
        ),
    ]
