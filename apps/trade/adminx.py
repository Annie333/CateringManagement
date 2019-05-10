
import xadmin
from .models import ShoppingCart, OrderInfo, OrderGoods


class ShoppingCartAdmin(object):
    list_display = ["user", "goods", "goods_num", "add_time"]
    search_fields = ["user__name", "goods__name", "goods_num"]
    list_filter = ["user__name", "goods__name", "goods_num", "add_time"]


class OrderInfoAdmin(object):
    list_display = ["user", "add_time", "order_sn", "trade_no", "pay_status", "order_mount","post_script", "pay_time",
                    "get_way", "get_time", "address", "signer_name", "signer_identity", "signer_mobile"]
    search_fields = ["user__name", "order_sn", "trade_no", "pay_status", "order_mount","post_script",
                     "get_way", "address", "signer_name", "signer_identity", "signer_mobile"]
    list_filter = ["user__name", "add_time", "order_sn", "trade_no", "pay_status", "order_mount", "post_script",
                   "pay_time",
                   "get_way", "get_time", "address", "signer_name", "signer_identity", "signer_mobile"]

    class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline, ]


xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
