# Generated by Django 2.0 on 2019-05-03 21:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_option', '0010_auto_20190501_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavingmessage',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 3, 21, 45, 48, 380280), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 3, 21, 45, 48, 380280), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usergoodsfav',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 3, 21, 45, 48, 380280), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userwindowsfav',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 3, 21, 45, 48, 380280), verbose_name='添加时间'),
        ),
    ]
