from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WishlistList, WishlistDetail, UserWishlistList, WishlistItemDelete

router = DefaultRouter()

urlpatterns = [
    path('wishlist/', WishlistList.as_view(), name='wishlist-list'),
    path('wishlist/<int:pk>/', WishlistDetail.as_view(), name='wishlist-detail'),
    path('user/wishlist/', UserWishlistList.as_view(), name='user-wishlist-list'),
    path('wishlist/item/<int:id>/remove/', WishlistItemDelete.as_view(), name='wishlist-item-delete'),
]
