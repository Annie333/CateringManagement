import django_filters
from django.db.models import Q
from users.models import Staff


class StaffFilter(django_filters.rest_framework.FilterSet):
    """
    员工的过滤类
    """

    class Meta:
        model = Staff
        fields = ['user', 'windows']
