# Generated by Django 2.2 on 2019-04-20 02:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_option', '0012_auto_20190420_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavingmessage',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 20, 10, 40, 50, 852576), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 20, 10, 40, 50, 852576), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 20, 10, 40, 50, 851576), verbose_name='添加时间'),
        ),
    ]
