from django.db import models
from django.contrib.auth import get_user_model
from DjangoUeditor.models import UEditorField
from datetime import datetime
# Create your models here.

User = get_user_model()


class PlaceCategory(models.Model):
    """
    食堂
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    place_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别", default="1")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    desc = UEditorField(verbose_name="类别描述", width=1000, height=300, default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "食堂类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Windows(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True, verbose_name="窗口名称")
    kind = models.ForeignKey(PlaceCategory,  related_name='brands', null=True, blank=True, verbose_name="窗口类目",
                             on_delete=models.CASCADE)
    windows_front_image = models.ImageField(upload_to="windows/", null=True, blank=True, verbose_name="窗口图")
    windows_desc = models.TextField(default="", max_length=200, verbose_name="类别描述", help_text="类别描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "食堂窗口"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    CATEGORY_TYPE = (
        (1, "主食"), (2, "配菜"), (3, "套餐"), (4, "饮品")
    )
    window = models.ForeignKey(Windows, verbose_name="所在窗口", on_delete=models.CASCADE)
    name = models.CharField(max_length=10, null=True, blank=True, verbose_name="菜品名称")
    price = models.IntegerField(default=0, null=True, blank=True, verbose_name="价格")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="菜品类别", help_text="菜品类别")
    goods_brief = models.TextField(max_length=500, default="", verbose_name="菜品简短描述")
    goods_desc = UEditorField(verbose_name="内容", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    num = models.IntegerField(null=True, blank=True, verbose_name="菜品份数", help_text="菜品库存")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="菜品销售量")
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    sex = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    mycode = models.CharField(max_length=15, null=True, blank=True, default="1234", verbose_name="密码")
    enter_date = models.DateField(null=True, blank=True, verbose_name="入职时间")
    window = models.ForeignKey(Windows, verbose_name="员工所在窗口", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IndexAd(models.Model):
    category = models.ForeignKey(PlaceCategory, related_name='category', verbose_name="商品类目", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, related_name='goods', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '首页窗口类别广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    轮播的商品
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    热搜词
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords
