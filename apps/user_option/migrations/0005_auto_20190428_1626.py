# Generated by Django 2.0 on 2019-04-28 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_option', '0004_auto_20190428_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavingmessage',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 28, 16, 26, 27, 916064), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 28, 16, 26, 27, 916064), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 28, 16, 26, 27, 916064), verbose_name='添加时间'),
        ),
    ]