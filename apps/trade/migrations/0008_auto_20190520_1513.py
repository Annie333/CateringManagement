# Generated by Django 2.0 on 2019-05-20 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0007_auto_20190520_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 20, 15, 13, 39, 260087), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 20, 15, 13, 39, 260087), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 20, 15, 13, 39, 260087), verbose_name='添加时间'),
        ),
    ]