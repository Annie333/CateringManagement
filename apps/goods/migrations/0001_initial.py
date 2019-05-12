# Generated by Django 2.0 on 2019-05-12 21:37

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner', verbose_name='轮播图片')),
                ('index', models.IntegerField(default=0, verbose_name='轮播顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '轮播商品',
                'verbose_name_plural': '轮播商品',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='菜品名称')),
                ('price', models.IntegerField(blank=True, default=0, null=True, verbose_name='价格')),
                ('category_type', models.IntegerField(choices=[(1, '主食'), (2, '配菜'), (3, '套餐'), (4, '饮品')], help_text='菜品类别', verbose_name='菜品类别')),
                ('goods_brief', models.TextField(default='', max_length=500, verbose_name='菜品简短描述')),
                ('goods_desc', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('num', models.IntegerField(blank=True, help_text='菜品库存', null=True, verbose_name='菜品份数')),
                ('goods_front_image', models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='封面图')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('sold_num', models.IntegerField(default=0, verbose_name='菜品销售量')),
                ('ship_free', models.BooleanField(default=True, verbose_name='是否承担运费')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热销')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新品')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
            },
        ),
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='热搜词')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '热搜词',
                'verbose_name_plural': '热搜词',
            },
        ),
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '首页窗口类别广告',
                'verbose_name_plural': '首页窗口类别广告',
            },
        ),
        migrations.CreateModel(
            name='PlaceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('code', models.CharField(default='', help_text='类别code', max_length=30, verbose_name='类别code')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], default='1', help_text='类目级别', verbose_name='类目级别')),
                ('is_tab', models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航')),
                ('desc', DjangoUeditor.models.UEditorField(default='', verbose_name='类别描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('place_category', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.PlaceCategory', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '食堂类别',
                'verbose_name_plural': '食堂类别',
            },
        ),
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
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
            },
        ),
        migrations.CreateModel(
            name='Windows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='窗口名称')),
                ('windows_front_image', models.ImageField(blank=True, null=True, upload_to='windows/', verbose_name='窗口图')),
                ('windows_desc', models.TextField(default='', help_text='类别描述', max_length=200, verbose_name='类别描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('kind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.PlaceCategory', verbose_name='窗口类目')),
            ],
            options={
                'verbose_name': '食堂窗口',
                'verbose_name_plural': '食堂窗口',
            },
        ),
        migrations.AddField(
            model_name='staff',
            name='windows',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='goods.Windows', verbose_name='员工所在窗口'),
        ),
        migrations.AddField(
            model_name='indexad',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='goods.PlaceCategory', verbose_name='商品类目'),
        ),
        migrations.AddField(
            model_name='indexad',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.Goods'),
        ),
        migrations.AddField(
            model_name='goods',
            name='window',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Windows', verbose_name='所在窗口'),
        ),
        migrations.AddField(
            model_name='banner',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品'),
        ),
    ]
