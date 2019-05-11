from _datetime import datetime
import xadmin
from .models import Goods, GoodsImage, Windows, Banner, HotSearchWords, Staff, PlaceCategory
from .models import IndexAd
import DjangoUeditor


class GoodsAdmin(object):
    list_display = ["name", "num", "click_num", "sold_num", "fav_num", "goods_brief", "goods_desc", "add_time",
                    "category_type", "window", "ship_free", "is_hot", "price", "is_new"]
    search_fields = ['name', "category_type", "window__name", "ship_free", "is_hot", "price", "is_new"]
    list_filter = ["name", "num", "click_num", "sold_num", "fav_num", "goods_brief", "goods_desc", "add_time",
                   "category_type", "window__name", "ship_free", "is_hot", "price", "is_new"]
    style_fields = {"goods_desc": "ueditor"}

    class GoodsImagesInline(object):
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]


class StaffAdmin(object):
    list_display = ['window', 'name', "birthday", "sex", "mobile", "enter_date"]
    list_filter = ['window__name', 'name', "birthday", "sex", "mobile", "enter_date"]
    search_fields = ['name', "window__name"]


class PlaceCategoryAdmin(object):
    list_display = ["name", "category_type", "place_category", "add_time"]
    list_filter = ["category_type", "place_category", "name"]
    search_fields = ['name', ]


class WindowsAdmin(object):
    list_display = ["name", "kind", "add_time", "windows_desc"]
    search_fields = ['name', "kind__name"]
    list_filter = ["name", "kind__name", "add_time", "windows_desc"]


class BannerGoodsAdmin(object):
    list_display = ["goods", "image", "index"]


class HotSearchAdmin(object):
    list_display = ["keywords", "index", "add_time"]


class IndexAdAdmin(object):
    list_display = ["category", "goods"]


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(Windows, WindowsAdmin)
xadmin.site.register(Staff, StaffAdmin)
xadmin.site.register(HotSearchWords, HotSearchAdmin)
xadmin.site.register(IndexAd, IndexAdAdmin)
xadmin.site.register(Banner, BannerGoodsAdmin)
xadmin.site.register(PlaceCategory,PlaceCategoryAdmin)
