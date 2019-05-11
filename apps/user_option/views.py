from django.shortcuts import render
from rest_framework import viewsets,mixins
from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin
from user_option.serializers import UserGoodsFavSerializer, UserWindowsFavSerializer
from user_option.models import UserWindowsFav, UserGoodsFav
from rest_framework.permissions import IsAuthenticated
from Utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

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


class UserWindowsFavViewSet(CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin, mixins.ListModelMixin):
    serializer_class = UserWindowsFavSerializer
    # queryset = UserWindowsFav.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = "windows_id"

    def get_queryset(self):
        return UserWindowsFav.objects.filter(user=self.request.user)
