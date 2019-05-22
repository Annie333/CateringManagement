
from django_filters.rest_framework import DjangoFilterBackend

from goods.serializers import GoodsSerializer, PlaceCategorySerializer, WindowsSerializer, BannerSerializer, \
    HotWordsSerializer, IndexCategorySerializer
from .models import Goods, PlaceCategory, Windows,  Banner, HotSearchWords
from rest_framework import mixins

from rest_framework import filters
from goods.filters import GoodsFilter, WindowsFilter

from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc',)
    ordering_fields = ('sold_num', 'price')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PlaceCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    商品分类数据
    retrieve:
    获取商品分类详情
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

class HotSearchsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer


class BannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取轮播图列表
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer


class IndexCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    queryset = PlaceCategory.objects.filter(name__in=["紫荆园", "玫瑰园"])
    serializer_class = IndexCategorySerializer
