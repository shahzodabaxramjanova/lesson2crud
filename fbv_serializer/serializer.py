from rest_framework import serializers
from products.models import Product
from rest_framework.exceptions import ValidationError


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        title = data.get('title')
        if title.isdigit():
            raise ValidationError({'error': 'title son bolmasligi kerak'})
        return data
    
    def validate_price(self, value):
        if value < 0:
            raise ValidationError({'error': 'narxni togri kiriting'})
        return value
    
    def validate_color(self, color):
        if not color.islower():
            raise ValidationError({'error': 'rangninkichkina harflarda yozing'})
        return color
    
    def validate_desc(self, desc):
        if desc.isdigit():
            raise ValidationError({'error': 'raqamlardan iborat bolmasin'})
        return desc