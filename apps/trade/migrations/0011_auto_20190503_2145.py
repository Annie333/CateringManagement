# Generated by Django 2.0 on 2019-05-03 21:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0010_auto_20190501_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 3, 21, 45, 48, 380280), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 3, 21, 45, 48, 380280), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 3, 21, 45, 48, 380280), verbose_name='添加时间'),
        ),
    ]