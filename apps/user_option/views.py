from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import viewsets,mixins
from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin
from user_option.serializers import UserGoodsFavSerializer, UserWindowsFavSerializer, AddressSerializer, \
    UserGoodsFavDetailSerializer, LeavingMessageSerializer, LeavingMessageDetailSerializer,StaffLeavingMessageSerializer
from user_option.models import UserWindowsFav, UserGoodsFav, UserAddress, LeavingMessage
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from user_option.filters import LeavingMessageFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

User = get_user_model()


# Create your views here.
class UserGoodsFavViewSet(CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin, mixins.ListModelMixin):
    serializer_class = UserGoodsFavSerializer
    # queryset = UserGoodsFav.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = "goods_id"    #设置查询哪个字段

    def get_queryset(self):
        return UserGoodsFav.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return UserGoodsFavDetailSerializer
        elif self.action == "create":
            return UserGoodsFavSerializer

        return UserGoodsFavSerializer


class UserWindowsFavViewSet(CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin, mixins.ListModelMixin):
    serializer_class = UserWindowsFavSerializer
    # queryset = UserWindowsFav.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = "windows_id"

    def get_queryset(self):
        return UserWindowsFav.objects.filter(user=self.request.user)


class LeavingMessageViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    list:
        获取用户留言
    create:
        添加留言
    delete:
        删除留言功能
    """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = LeavingMessageSerializer
    lookup_field = "windows_id"

    def get_queryset(self):
        return LeavingMessage.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return LeavingMessageDetailSerializer
        elif self.action == "create":
            return LeavingMessageSerializer

        return LeavingMessageSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    收货地址管理
    list:
        获取收货地址
    create:
        添加收货地址
    update:
        更新收货地址
    delete:
        删除收货地址
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


class StaffMessageViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        员工获取用户留言
    """

    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = LeavingMessage.objects.all()
    serializer_class = StaffLeavingMessageSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_class = LeavingMessageFilter
