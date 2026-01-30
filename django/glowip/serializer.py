from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.Serializer):
    class Meta:
        model= Product
        fields=['id','product_name','product_type','brand','notable_effects','skin_type','price','picture_src','description','rating']