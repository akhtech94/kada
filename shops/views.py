from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Shop
from products.serializers import ProductSerializer
from .serializers import ShopSerializer
from rest_framework.response import Response

class AddShopView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data            = self.request.data
        name            = data['name']
        streetAddress   = data['streetAddress']
        district        = data['district']
        state           = data['state']
        country         = data['country']
        pincode         = data['pincode']
        phoneNumber1    = data['phoneNumber1']

        Shop.objects.create(
            name=name,
            streetAddress=streetAddress,
            district=district,
            state=state,
            country=country,
            pincode=pincode,
            phoneNumber1=phoneNumber1,
        )

        return Response({"Success": "Shop added to the databse"})

class ShopsListView(ListAPIView):
    permission_classes  = (permissions.AllowAny,)
    queryset            = Shop.objects.all()
    serializer_class    = ShopSerializer
    pagination_class    = None

class ShopProductsView(ListAPIView):
    permission_classes  = (permissions.AllowAny,)
    # shop                = Shop.objects.get(id=1)
    # queryset            = shop.product_set.all()
    # serializer_class    = ProductSerializer
    pagination_class    = None
