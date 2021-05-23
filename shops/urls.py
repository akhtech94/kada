from django.urls import path
from .views import(
    ShopProductAddView,
    ShopsListView,
    ShopProductsView,
    AddShopView,
) 

urlpatterns = [
    path('', ShopsListView.as_view()),
    path('shop-products-list', ShopProductsView.as_view()),
    path('add-shop', AddShopView.as_view()),
    path('add-shop-product', ShopProductAddView.as_view()),
]
