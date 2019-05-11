import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator
from CateringManagement.settings import REGEX_MOBILE

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """

        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        return mobile


class UserRegSerializer(serializers.ModelSerializer):
    """用户"""
    identities = serializers.CharField(required=True, write_only=True, max_length=9, min_length=9,
                                       error_messages={
                                           "blank": "请输入身份号码",
                                           "required": "请输入身份号码",
                                           "max_length": "格式错误",
                                           "min_length": "格式错误"
                                       },
                                       help_text="身份号码")
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )

    # def create(self, validated_data):
    #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    def validate_identities(self, identities):
        verify_records = User.objects.filter(mobile=self.initial_data["username"])
        if verify_records:
            raise serializers.ValidationError("用户已存在")
        return identities

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        # attrs["identities"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "identities", "mobile", "password")


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = User
        fields = ("name", "gender", "birthday", "email", "mobile")


class UserSerializer(serializers.ModelSerializer):
    identities = serializers.CharField(required=True, write_only=True, max_length=4, min_length=9, label="身份号码",
                                       error_messages={
                                           "blank": "请输入身份号码",
                                           "required": "请输入身份号码",
                                           "max_length": "格式错误",
                                           "min_length": "格式错误"
                                       },
                                       help_text="验证码")
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["identities"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "code", "mobile", "password")