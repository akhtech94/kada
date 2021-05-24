from rest_framework.response import Response
from shops.models import Shop
from .models import Product

def addProduct(data):
    shop = Shop.objects.get(id=data['shop_id'])    
    product = Product(
        name        = data['name'],
        available   = data['available'],
        rate        = data['rate'],
        shop        = shop,
    )

    for key , value in data.items():
        if key == 'quality':
            product.quality = value
        elif key == 'colour':
            product.colour = value
        elif key == "specification":
            product.specification = value

    product.save()
    return True

def deleteProduct(data, shop):
    try:
        product = shop.product_set.get(id=data['product_id'])
    except:
        return False
    product.delete()
    return True

def updateProduct(data, shop):
    try:
        product = shop.product_set.get(id=data['product_id'])
    except:
        return False
    for key, value in data.items():
        if key == 'name':
            product.name = data['name']
        elif key == 'available':
            product.available = data['available']
        elif key == 'rate':
            product.rate = data['rate']
        elif key == 'quality':
            product.quality = data['quality']
        elif key == 'colour':
            product.colour = data['colour']
        elif key == 'specification':
            product.specification = data['specification']
    product.save()
    return Response( {"Success": "Product updated successfully"} )
