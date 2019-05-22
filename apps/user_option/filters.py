import django_filters
from django.db.models import Q
from user_option.models import LeavingMessage


class LeavingMessageFilter(django_filters.rest_framework.FilterSet):
    """
    留言的过滤类
    """
    # windows_filter = django_filters.NumberFilter(method="windows_filter")
    #
    # def windows_filter(self, queryset, name, value):
    #     return queryset.filter(Q(windows_id=value))

    class Meta:
        model = LeavingMessage
        fields = ['windows', ]
