import time
from rest_framework import serializers
from rest_framework import mixins
from goods.models import Goods,Windows
from .models import ShoppingCart, OrderInfo, OrderGoods
from goods.serializers import GoodsSerializer


# from utils.alipay import AliPay
# from MxShop.settings import private_key_path, ali_pub_key_path


class ShopCartDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = ShoppingCart
        fields = "__all__"


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

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

    def update(self, instance, validated_data):
        """修改商品数量"""
        instance.goods_num = validated_data["goods_num"]
        instance.save()
        return instance


class ShopCartDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ("goods", "goods_num")


class OrderGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False)

    class Meta:
        model = OrderGoods
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)

    def generate_order_sn(self):
        # 当前时间+userid+随机数
        from random import Random
        random_ins = Random()
        order_sn = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                       userid=self.context["request"].user.id,
                                                       ranstr=random_ins.randint(10, 99))

        return order_sn

    def validate(self, attrs):
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    class Meta:
        model = OrderInfo
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = "__all__"
