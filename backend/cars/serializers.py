from rest_framework import serializers
from .models import Car, CarImage

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['id', 'image']

class CarSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), required=False, write_only=True)
    uploaded_images = CarImageSerializer(many=True, read_only=True, source='images')

    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'year', 'price', 'km', 'fuel', 'transmission', 'description', 'status', 'images', 'uploaded_images']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
