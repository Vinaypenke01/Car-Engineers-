from .models import Car, CarImage

class CarService:
    @staticmethod
    def create_car(validated_data):
        images_data = validated_data.pop('images', [])
        car = Car.objects.create(**validated_data)
        for image_data in images_data:
            CarImage.objects.create(car=car, image=image_data)
        return car

    @staticmethod
    def update_car(instance, validated_data):
        images_data = validated_data.pop('images', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if images_data is not None:
            instance.images.all().delete()
            for image_data in images_data:
                CarImage.objects.create(car=instance, image=image_data)
        
        return instance
