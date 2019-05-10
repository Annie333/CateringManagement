# Generated by Django 2.0 on 2019-04-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodscategory',
            name='category_type',
        ),
        migrations.RemoveField(
            model_name='goodscategory',
            name='code',
        ),
        migrations.RemoveField(
            model_name='goodscategory',
            name='is_tab',
        ),
        migrations.RemoveField(
            model_name='goodscategory',
            name='parent_category',
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='name',
            field=models.IntegerField(choices=[(1, '饭'), (2, '面'), (3, '早餐类'), (4, '夜宵'), (5, '综合')], help_text='窗口类别', verbose_name='窗口类别'),
        ),
    ]