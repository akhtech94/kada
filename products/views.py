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