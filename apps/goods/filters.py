import django_filters
from django.db.models import Q

from goods.models import Goods,Windows, PlaceCategory


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(field_name='price', help_text="最低价格", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    top_category = django_filters.NumberFilter(method="top_category_filter")

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(window_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'is_hot']


class WindowsFilter(django_filters.rest_framework.FilterSet):
    """
    窗口类别的过滤类
    """
    top_category = django_filters.NumberFilter(method="top_category_filter")

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(
            Q(kind_id=value) | Q(kind__place_category_id=value) | Q(kind__place_category__place_category_id=value))

    class Meta:
        model = Windows
        fields = ["kind_id"]
