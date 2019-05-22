from django.shortcuts import render

from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, authentication
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.mixins import CreateModelMixin
from .serializers import UserRegSerializer,UserDetailSerializer, StaffDetailSerializer
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework import permissions
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from users.models import Staff
from  users.filters import StaffFilter
User = get_user_model()
# Create your views here.


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewSet(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户注册
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer

        return UserDetailSerializer

    # permission_classes = (permissions.IsAuthenticated, JS)
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []

        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.perform_create(serializer)
        # self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def get_object(self):
        return self.request.user#用户随意传递数字，只返回自身用户id


class StaffViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = StaffFilter
