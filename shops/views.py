from products.models import Product
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Shop
from products.serializers import ProductSerializer
from .serializers import ShopSerializer
from rest_framework.response import Response
from products.views import addProduct

class AddShopView(APIView):

    def post(self, format=None):
        user            = self.request.user
        if not user.is_shop:
            return Response({"Error": "Inappropriate account for adding a shop."})
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
            owner=user,
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

class ShopProductAddView(APIView):

    def post(self, request):
        shop = Shop.objects.get(id=self.request.data['shop_id'])
        if shop == None:
            return Response( {"Error": "The shop you are trying to add product to does not exist."})
        if shop.owner != self.request.user:
            return Response( {"Error": "Sorry you can add products only to your shops !!!"} )
        data = self.request.data
        status = addProduct(data)
        if status:
            return Response({"Success": "Product added successfully"})
        return Response( {"Error": "This shop doesn't exist"} )
