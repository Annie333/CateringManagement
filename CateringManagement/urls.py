"""CateringManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from CateringManagement.settings import MEDIA_ROOT
from django.views.static import serve
from goods.views import GoodsListViewSet, PlaceCategoryViewSet, WindowsListViewSet, BannerViewSet, HotSearchsViewSet, \
    IndexCategoryViewSet
from trade.views import ShoppingCartViewSet, OrderViewSet, AlipayView
from users.views import UserViewSet, StaffViewSet
import xadmin
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from user_option.views import UserWindowsFavViewSet, UserGoodsFavViewSet, AddressViewSet, LeavingMessageViewSet, \
    StaffMessageViewSet
from rest_framework_jwt.views import refresh_jwt_token

router = DefaultRouter()
router.register(r'goods', GoodsListViewSet, base_name="goods")
router.register(r'categorys', PlaceCategoryViewSet, base_name="categorys")
router.register(r'windows', WindowsListViewSet, base_name="windows")
router.register(r'users', UserViewSet, base_name="users")
router.register(r'windowsfav', UserWindowsFavViewSet, base_name="windowsfav")
router.register(r'goodsfav', UserGoodsFavViewSet, base_name="goodsfav")
router.register(r'messages', LeavingMessageViewSet, base_name="message")
router.register(r'address', AddressViewSet, base_name="address")
# router.register(r'staff', StaffViewSet, base_name="staff")
router.register(r'shopcarts', ShoppingCartViewSet, base_name="shopcarts")
router.register(r'orders', OrderViewSet, base_name="orders")
router.register(r'banners', BannerViewSet, base_name='banners')
router.register(r'hotsearchs', HotSearchsViewSet, base_name='hotsearchs')
router.register(r'indexgoods', IndexCategoryViewSet, base_name='indexgoods')
router.register(r'staffmessage', StaffMessageViewSet, base_name='staffmessage')
router.register(r'staff', StaffViewSet, base_name='staff')
goods_list = GoodsListViewSet.as_view({
    'get': 'list',
})

#配置goods的url
urlpatterns = [
    url(r'xadmin/', xadmin.site.urls),
    url(r'', include(router.urls)),
    url(r'docs/', include_docs_urls(title="食堂管理")),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # jwt的认证接口
    url(r'^api-token-auth/', views.obtain_auth_token),
    #drf自带认证接口
    url(r'^login/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),

    url(r'^alipay/return/', AlipayView.as_view(), name="alipay"),
]
