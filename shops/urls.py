from django.urls import path
from .views import ShopsListView, ShopProductsView

urlpatterns = [
    path('', ShopsListView.as_view()),
    path('productslist', ShopProductsView.as_view()),
]