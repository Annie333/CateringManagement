# Generated by Django 2.0 on 2019-05-10 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0027_auto_20190510_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 10, 18, 13, 12, 547464), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 10, 18, 13, 12, 547464), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 5, 10, 18, 13, 12, 547464), verbose_name='添加时间'),
        ),
    ]