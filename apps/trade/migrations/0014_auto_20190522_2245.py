# Generated by Django 2.0 on 2019-05-22 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0013_auto_20190522_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 22, 22, 45, 0, 908762), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 22, 22, 45, 0, 907760), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 22, 22, 45, 0, 906758), verbose_name='添加时间'),
        ),
    ]