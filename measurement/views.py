# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer

# @api_view(['GET'])
# def func(request):
#     data = {'message': 200}
#     return Response(data)

class Sensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        sensor = Sensor()
        sensor.name = 'ESP32'
        sensor.description = 'Датчик на кухне за холодильником'
        sensor.save()
        data = {
            'name': sensor.name,
            'description': sensor.description,
        }
        return Response(data)

    def patch(self, request, id):
        sensor = Sensor.objects.all(id=id)
        print(sensor)
        sensor.description = 'Перенес датчик на балкон'
        data = {'description': sensor.description}
        return Response(data)

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementAdd(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        measurement = Measurement()
        measurement.id = 1
        measurement.temperature = 22.3
        data = {
            'sensor': measurement.sensor,
            'temperature': measurement.temperature,
        }
        return Response(data)





    # def patch(self, request, id):
    #     sensor = Sensor.objects.all(id=1)
    #     sensor.description = 'Перенес датчик на балкон'
    #     data = {'description': sensor.description}
    #     return Response(data)

