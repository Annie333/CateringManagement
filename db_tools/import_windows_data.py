#独立使用django的model
import sys
import os
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CateringManagement.settings')

import django
django.setup()


from goods.models import Windows
from  goods.models import GoodsCategory
from db_tools.data.window_data import row_data

for windows_detail in row_data:
    windows = Windows()
    windows.name = windows_detail["name"]
    windows.windows_desc = windows_detail['windows_desc'] if windows_detail["windows_desc"] is not None else ""
    windows.windows_front_image = windows_detail['images'][0] if windows_detail['images'] is not None else ""

    kind_name = windows_detail["kind"][-1]
    kind = GoodsCategory.objects.filter()
    if kind:
        windows.kind = kind[0]
    windows.save()
