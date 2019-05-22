from rest_framework import serializers
from .models import Goods, Windows, PlaceCategory, GoodsImage, Banner, HotSearchWords, IndexAd
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q


class PlaceCategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = PlaceCategory
        fields = "__all__"


class PlaceCategorySerializer2(serializers.ModelSerializer):
    sub_cat = PlaceCategorySerializer3(many=True)

    class Meta:
        model = PlaceCategory
        fields = "__all__"


class PlaceCategorySerializer(serializers.ModelSerializer):
    sub_cat = PlaceCategorySerializer2(many=True)

    class Meta:
        model = PlaceCategory
        fields = "__all__"


class WindowsSerializer(serializers.ModelSerializer):
    kind = PlaceCategorySerializer2()

    class Meta:
        model = Windows
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):
    window = WindowsSerializer()
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"


class HotWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSearchWords
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class IndexCategorySerializer(serializers.ModelSerializer):
    windows = WindowsSerializer(many=True)
    goods = serializers.SerializerMethodField()
    sub_cat = PlaceCategorySerializer2(many=True)
    ad_goods = serializers.SerializerMethodField()

    def get_ad_goods(self, obj):
        goods_json = {}
        ad_goods = IndexAd.objects.filter(window_id=obj.id, )
        if ad_goods:
            good_ins = ad_goods[0].goods
            goods_json = GoodsSerializer(good_ins, many=False, context={'request': self.context['request']}).data
        return goods_json

    def get_goods(self, obj):
        all_goods = Goods.objects.filter(Q(window_id=obj.id) | Q(window__kind_id=obj.id) | Q(
            window__kind__place_category_id=obj.id))
        goods_serializer = GoodsSerializer(all_goods, many=True, context={'request': self.context['request']})
        return goods_serializer.data

    class Meta:
        model = PlaceCategory
        fields = "__all__"
