# Generated by Django 2.0 on 2019-05-12 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0010_auto_20190512_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='姓名')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生年月')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6, verbose_name='性别')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='电话')),
                ('code', models.IntegerField(default='1234', verbose_name='密码')),
                ('enter_date', models.DateField(blank=True, null=True, verbose_name='入职时间')),
                ('windows', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='goods.Windows', verbose_name='员工所在窗口')),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
            },
        ),
    ]
