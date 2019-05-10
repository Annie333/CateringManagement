from rest_framework import serializers
from .models import Goods, Windows, PlaceCategory, GoodsImage


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
    kind = PlaceCategorySerializer()

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


