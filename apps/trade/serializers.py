import time
from rest_framework import serializers

from goods.models import Goods
from .models import ShoppingCart, OrderInfo, OrderGoods
from goods.serializers import GoodsSerializer


# from utils.alipay import AliPay
# from MxShop.settings import private_key_path, ali_pub_key_path


# class ShopCartDetailSerializer(serializers.ModelSerializer):
#     goods = GoodsSerializer(many=False, read_only=True)
#
#     class Meta:
#         model = ShoppingCart
#         fields = ("goods", "nums")


class ShopCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    goods_num = serializers.IntegerField(required=True, label="数量", min_value=1,
                                         error_messages={
                                             "min_value": "商品数量不能小于一",
                                             "required": "请选择购买数量"
                                         })
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    def create(self, validated_data):
        user = self.context["request"].user
        goods_num = validated_data["goods_num"]
        goods = validated_data["goods"]

        existed = ShoppingCart.objects.filter(user=user, goods=goods)

        if existed:
            existed = existed[0]
            existed.goods_num += goods_num
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)

        return existed




