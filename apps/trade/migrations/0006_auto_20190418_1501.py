# Generated by Django 2.2 on 2019-04-18 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0005_auto_20190418_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odergoods',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 18, 15, 1, 32, 344852), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 18, 15, 1, 32, 344852), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 18, 15, 1, 32, 344852), verbose_name='添加时间'),
        ),
    ]
