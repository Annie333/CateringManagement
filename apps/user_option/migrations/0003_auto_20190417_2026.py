# Generated by Django 2.2 on 2019-04-17 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_option', '0002_auto_20190417_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leavingmessage',
            old_name='mesg_type',
            new_name='msg_type',
        ),
        migrations.AlterField(
            model_name='leavingmessage',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 17, 20, 25, 53, 815670), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 17, 20, 25, 53, 816671), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2019, 4, 17, 20, 25, 53, 815670), verbose_name='添加时间'),
        ),
    ]