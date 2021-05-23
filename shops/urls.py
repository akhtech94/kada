from django.urls import path
from .views import ShopsListView, ShopProductsView, AddShopView

urlpatterns = [
    path('', ShopsListView.as_view()),
    path('shop-products-list', ShopProductsView.as_view()),
    path('add-shop', AddShopView.as_view()),
]