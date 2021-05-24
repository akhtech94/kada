from django.urls import path
from .views import(
    ShopsListView,
    ShopProductsView,
    AddShopView,
    DeleteShopView,
    ShopProductAddView,
    ShopProductUpdateView,
    ShopProductDeleteView,
) 

urlpatterns = [
    path('', ShopsListView.as_view()),
    path('shop-products-list', ShopProductsView.as_view()),
    path('add-shop', AddShopView.as_view()),
    path('delete-shop', DeleteShopView.as_view()),
    path('add-shop-product', ShopProductAddView.as_view()),
    path('update-shop-product', ShopProductUpdateView.as_view()),
    path('delete-shop-product', ShopProductDeleteView.as_view()),
]
