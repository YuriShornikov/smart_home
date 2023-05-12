from django.urls import path

from measurement.views import Sensors, SensorsView, Measurements

urlpatterns = [
    path('sensors/', Sensors.as_view()),
    path('measurements/', Measurements.as_view()),
    path('sensors/<pk>/', SensorsView.as_view()),
]
