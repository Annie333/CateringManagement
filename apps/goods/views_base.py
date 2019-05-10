from django.views.generic.base import View
from  goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        jason_list = []
        goods =Goods.objects.all()[:10]
        # for good in goods:
        #
        #     jason_dict = {}
        #     jason_dict["name"]=good.name
        #     jason_dict["price"] = good.price
        #     jason_dict["goods_brief"] = good.goods_desc
        #     jason_dict["add_time"] = good.add_time
        #     jason_list.append(jason_dict)

        # from django.forms.models import model_to_dict
        # for good in goods:
        #     jason_dict = model_to_dict(good)
        #     jason_list.append(jason_dict)
        import json
        from django.core import serializers
        jason_data = serializers.serialize("json", goods)
        jason_data = json.loads(jason_data)

        from django.http import HttpResponse, JsonResponse
        import json
        return JsonResponse(jason_data, safe=False)

