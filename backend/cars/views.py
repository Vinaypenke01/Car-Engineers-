from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from .services import CarService

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        car = CarService.create_car(serializer.validated_data)
        
        response_serializer = CarSerializer(car)
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        car = CarService.update_car(instance, serializer.validated_data)
        return Response(CarSerializer(car).data)
