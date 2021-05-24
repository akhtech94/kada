from products.models import Product
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Shop
from products.serializers import ProductSerializer
from .serializers import ShopSerializer
from rest_framework.response import Response
from products.views import addProduct, deleteProduct, updateProduct

class AddShopView(APIView):

    def post(self, request):
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

class UpdateShopView(APIView):

    def post(self, request):
        user = self.request.user
        try:
            shop = Shop.objects.get(id=self.request.data['shop_id'])
        except:
            return Response( {"Error": "This shop does not exist"} )
        if user != shop.owner:
            return Response( {"Error": "Sorry. You cannot update details of other's shops."} )
        for key, value in self.request.data.items():
            if key == 'name':
                shop.name = self.request.data['name']
            elif key == 'landmark':
                shop.landmark = self.request.data['landmark']
            elif key == 'streetAddress':
                shop.streetAddress = self.request.data['streetAddress']
            elif key == 'district':
                shop.district = self.request.data['district']
            elif key == 'state':
                shop.state = self.request.data['state']
            elif key == 'country':
                shop.country = self.request.data['country']
            elif key == 'pincode':
                shop.pincode = self.request.data['pincode']
            elif key == 'phoneNumber1':
                shop.phoneNumber1 = self.request.data['phoneNumber1']
            elif key == 'phoneNumber2':
                shop.phoneNumber2 = self.request.data['phoneNumber2']
            elif key == 'dateJoined':
                shop.dateJoined = self.request.data['dateJoined']
            elif key == 'category':
                shop.category = self.request.data['category']
            elif key == 'gst':
                shop.gst = self.request.data['gst']
            elif key == 'licenseno':
                shop.licenseno = self.request.data['licenseno']
            elif key == 'is_active':
                shop.is_active = self.request.data['is_active']
        shop.save()
        return Response( {"Success": "Shop details updated successfully."} )
            

class DeleteShopView(APIView):
    def delete(self, request):
        shop=Shop.objects.get(id=self.request.data['id'])
        if self.request.user != shop.owner:
            return Response( {"Error": "You cannot remove other's shop !!!"} )
        if shop == None:
            return Response( {"Error": "The requested shop doesn't exist"} )
        shop.delete()
        return Response( {"Success": "The shop was deleted successfully"} )


class ShopProductAddView(APIView):

    def post(self, request):
        try:
            shop = Shop.objects.get(id=self.request.data['shop_id'])
        except:
            return Response( {"Error": "The shop you are trying to add product to does not exist."})
        if shop.owner != self.request.user:
            return Response( {"Error": "Sorry you can add products only to your shops !!!"} )
        data = self.request.data
        status = addProduct(data)
        if status:
            return Response({"Success": "Product added successfully"})
        return Response( {"Error": "This shop doesn't exist"} )

class ShopProductsView(ListAPIView):
    permission_classes  = (permissions.AllowAny,)
    # shop                = Shop.objects.get(id=1)
    # queryset            = shop.product_set.all()
    # serializer_class    = ProductSerializer
    pagination_class    = None

class ShopProductUpdateView(APIView):
    def post(self, request):
        user = self.request.user
        try:
            shop = Shop.objects.get(id=self.request.data['shop_id'])
        except:
            return Response( {"Error": "The shop does not exist"} )
        if user != shop.owner:
            return Response( {"Error": "Sorry. You cannot update products in other's shops"} )
        if not updateProduct(self.request.data, shop):
            return Response( {"Error": "The requested product could not be found."} )
        else:
            return Response( {"Succes": "The Product has been updated"} )

class ShopProductDeleteView(APIView):

    def delete(self, request):
        try:
            shop = Shop.objects.get(id=self.request.data['shop_id'])
        except :
            return Response( {'Error': "This shop does not exist in our database"} )
        if self.request.user != shop.owner:
            return Response( {"Error": "Sorry. You cannot delete products from other's shops."} )
        if not deleteProduct(self.request.data, shop):
            return Response( {"Error": "This product does not exist in your shop."})
        return Response( {"Success": "Product successfully removed from your shop."})
