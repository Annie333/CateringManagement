# Generated by Django 2.0 on 2019-05-20 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_option', '0008_auto_20190520_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 20, 16, 19, 8, 712486), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 20, 16, 19, 8, 712486), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usergoodsfav',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 20, 16, 19, 8, 712486), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userwindowsfav',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 20, 16, 19, 8, 712486), verbose_name='添加时间'),
        ),
    ]
