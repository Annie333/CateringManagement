# Generated by Django 2.0 on 2019-05-12 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_option', '0042_auto_20190512_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavingmessage',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 12, 9, 13, 56, 816123), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 12, 9, 13, 56, 816123), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usergoodsfav',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 12, 9, 13, 56, 800498), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userwindowsfav',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 12, 9, 13, 56, 816123), verbose_name='添加时间'),
        ),
    ]