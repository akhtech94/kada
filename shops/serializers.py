from rest_framework.serializers import ModelSerializer
from .models import Shops

class ShopsSerializer(ModelSerializer):
    class Meta:
        model = Shops
        fields = '__all__'
