from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ImageViewSet, ProductViewSet, ProductListByCategory, ProductList

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'images', ImageViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/category/<int:category_id>/', ProductListByCategory.as_view(), name='product-list-by-category'),
    path('products/search/', ProductList.as_view(), name='product-list-search'),
]
