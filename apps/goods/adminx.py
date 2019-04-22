from _datetime import datetime
import xadmin
from .models import Goods, GoodsCategory, GoodsImage, Windows, Banner, HotSearchWords
from .models import IndexAd
import DjangoUeditor


class GoodsAdmin(object):
    list_display = ["name", "num", "click_num", "sold_num", "fav_num", "goods_brief", "goods_desc",
                    "category_type"]
    search_fields = ['name', "category_type"]
    list_filter = ["name", "num", "click_num", "sold_num", "fav_num", "goods_brief", "goods_desc",
                   "category_type"]
    style_fields = {"goods_desc": "ueditor"}


class GoodsCategoryAdmin(object):
    list_display = ["name", "desc", " category_type", "is_tab", "add_time"]
    search_fields = ['name', "category_type"]
    list_filter =["name", "desc", " category_type", "is_tab", "add_time"]
    style_fields = {"desc": "ueditor"}


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)


