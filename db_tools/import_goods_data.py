#独立使用django的model
import sys
import os
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CateringManagement.settings')

import django
django.setup()


from goods.models import Goods
from  goods.models import Windows
from db_tools.data.product_data import row_data

for goods_detail in row_data:
    goods = Goods()
    goods.name = goods_detail["name"]
    goods.price = float(int(goods_detail["price"].replace("￥", "").replace("元", "")))
    goods.goods_brief = goods_detail["desc"] if goods_detail["desc"] is not None else ""
    goods.goods_desc = goods_detail["goods_desc"] if goods_detail["goods_desc"] is not None else ""
    goods.goods_front_image = goods_detail["images"][0] if goods_detail['images'] is not None else ""

    windows_name = goods_detail["windows"][-1]
    windows = goods.objects.filter()
    if windows:
        goods.window = windows[0]
    goods.save()
