# Generated by Django 2.2 on 2019-04-18 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_option', '0009_auto_20190418_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavingmessage',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 18, 19, 56, 49, 863391), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 18, 19, 56, 49, 863391), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 18, 19, 56, 49, 863391), verbose_name='添加时间'),
        ),
    ]