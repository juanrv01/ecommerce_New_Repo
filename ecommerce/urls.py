from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.views  import CategoryViewSet, ProductViewSet ,ProductListByCategory ,ProductList
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from wishlist.views import WishlistList, WishlistDetail ,UserWishlistList ,WishlistItemDelete
# from orders.views import PaymentView 
# from orders.views import CreateCheckOutSession ,stripe_webhook_view
from payment.views import PaymentView ,my_webhook_view

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('category/<int:category_id>/products', ProductListByCategory.as_view(), name='product_list_by_category'),
    path('wishlist', WishlistList.as_view(), name='wishlist-list'),
    path('wishlist/<int:pk>/', WishlistDetail.as_view(), name='wishlist-detail'),
    path('user/wishlist', UserWishlistList.as_view(), name='user-wishlist-list'),
    path('wishlist/product/<int:id>/', WishlistItemDelete.as_view(), name='remove-from-wishlist'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('api/webhook', my_webhook_view, name='stripe_webhook'),
    path('orders/', include('orders.urls')),
    path('auth/', include('users.urls')),
    path('cart/', include('cart.urls')),
    path('users/', include('users.urls')),
    path('doc_api/', include('docs.urls')),
 ]
