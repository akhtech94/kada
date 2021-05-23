from rest_framework.generics import ListAPIView
from rest_framework import permissions
from.models import Shop
from .serializers import ShopSerializer

class ShopListView(ListAPIView):
    permission_classes  = (permissions.AllowAny,)
    queryset            = Shop.objects.all()
    serializer_class    = ShopSerializer
    pagination_class    = None
