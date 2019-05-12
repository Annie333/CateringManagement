from rest_framework import serializers
from .models import Goods, Windows, PlaceCategory, GoodsImage, Staff
from rest_framework import status
from rest_framework.response import Response

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


class StaffSerializer(serializers.ModelSerializer):
    windows = serializers.PrimaryKeyRelatedField(required=True, queryset=Windows.objects.all())

    def validate_code(self, validated_data):
        mobile = validated_data["mobile"]
        code = validated_data["code"]
        windows = validated_data["windows"]
        content = {'please move along': '登录成功'}
        exists = Staff.objects.filter(mobile=mobile, code=code, windows=windows)
        if exists:
            return Response(content, status=status.HTTP_200_OK)
        else:
            raise serializers.ValidationError("用户不存在，请重新输入")

    class Meta:
        model = Staff
        fields = "__all__"
