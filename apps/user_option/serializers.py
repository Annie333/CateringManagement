from rest_framework import serializers
from .models import UserGoodsFav, UserWindowsFav, UserAddress, LeavingMessage, Goods, Windows
from goods.serializers import GoodsSerializer, WindowsSerializer
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.permissions import IsAuthenticated
from goods.serializers import GoodsSerializer


class UserGoodsFavSerializer(serializers.ModelSerializer):
    # goods = GoodsSerializer()
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    goods = serializers.PrimaryKeyRelatedField(required=True, many=True, queryset=Goods.objects.all())

    class Meta:
        model = UserGoodsFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserGoodsFav.objects.all(),
                fields=('user', 'goods'),
                message="已收藏过该商品"
            )
        ]
        fields = ("user", "goods", "id")#id用于取消收藏


class UserWindowsFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserWindowsFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserWindowsFav.objects.all(),
                fields=('user', 'windows'),
                message="已收藏过该窗口"
            )
        ]
        fields = ("user", "windows", "id")#id用于取消收藏


class LeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = LeavingMessage
        fields = ("user", "msg_type", "subject", "message", "file", "id", "add_time", "windows")


class LeavingMessageDetailSerializer(serializers.ModelSerializer):
    windows = WindowsSerializer()
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = LeavingMessage
        fields = ("msg_type", "subject", "message", "file", "id", "add_time", "windows")


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserAddress
        fields = ("id", "user", "district", "address", "signer_name", "add_time", "signer_mobile", "province", "city",
                  "signer_identity")


class UserGoodsFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = UserGoodsFav
        fields = ("goods", "id")


class StaffLeavingMessageSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )
    windows = serializers.PrimaryKeyRelatedField(required=True, queryset=Windows.objects.all())
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = LeavingMessage
        fields = ("user", "msg_type", "subject", "message", "file", "id", "add_time", "windows")
