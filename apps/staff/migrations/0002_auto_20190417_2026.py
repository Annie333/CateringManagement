# Generated by Django 2.2 on 2019-04-17 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='code',
            new_name='mycode',
        ),
    ]