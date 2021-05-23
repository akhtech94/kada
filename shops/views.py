from rest_framework.generics import ListAPIView
from rest_framework import permissions
from .models import Shops
from products.serializers import ProductsSerializer
from .serializers import ShopsSerializer

class ShopsListView(ListAPIView):
    permission_classes  = (permissions.AllowAny,)
    queryset            = Shops.objects.all()
    serializer_class    = ShopsSerializer
    pagination_class    = None

class ShopProductsView(ListAPIView):
    permission_classes  = (permissions.AllowAny,)
    shop                = Shops.objects.get(id=1)
    queryset            = shop.products_set.all()
    serializer_class    = ProductsSerializer
    pagination_class    = None