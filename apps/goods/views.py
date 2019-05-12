from coreapi.auth import TokenAuthentication
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.views import APIView
from goods.serializers import GoodsSerializer, PlaceCategorySerializer, WindowsSerializer
from rest_framework.response import Response
from .models import Goods, PlaceCategory, Windows, Staff
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from goods.filters import GoodsFilter, WindowsFilter
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework import status

# Create your views here.


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc',)
    ordering_fields = ('sold_num', 'price')


class PlaceCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    商品分类数据
    """

    queryset = PlaceCategory.objects.filter(category_type=1)
    serializer_class = PlaceCategorySerializer


class WindowsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    窗口数据
    """
    queryset = Windows.objects.all()
    serializer_class = WindowsSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = WindowsFilter
    search_fields = ('name', )


# class StaffViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     员工登录
#     """
#     queryset = Staff.objects.all()
#     serializer_class = StaffSerializer

# class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     获取热搜词列表
#     """
#     queryset = HotSearchWords.objects.all().order_by("-index")
#     serializer_class = HotWordsSerializer
#
#
# class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     获取轮播图列表
#     """
#     queryset = Banner.objects.all().order_by("index")
#     serializer_class = BannerSerializer
