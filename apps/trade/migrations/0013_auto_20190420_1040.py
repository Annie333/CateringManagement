# Generated by Django 2.2 on 2019-04-20 02:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0012_auto_20190420_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 20, 10, 40, 50, 850575), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 20, 10, 40, 50, 849574), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 20, 10, 40, 50, 849574), verbose_name='添加时间'),
        ),
    ]