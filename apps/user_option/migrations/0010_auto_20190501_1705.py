# Generated by Django 2.0 on 2019-05-01 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_option', '0009_auto_20190430_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavingmessage',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 1, 17, 5, 44, 458700), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 1, 17, 5, 44, 458700), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usergoodsfav',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 1, 17, 5, 44, 458700), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userwindowsfav',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 1, 17, 5, 44, 458700), verbose_name='添加时间'),
        ),
    ]