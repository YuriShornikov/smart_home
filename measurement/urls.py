from django.urls import path

from measurement import admin
from measurement.views import SensorView, Sensors, MeasurementAdd

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('sensors/', Sensors.as_view()),
    # path('sensors/<pk>/', SensorGET.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementAdd.as_view()),
    # path('func/', func),
    # TODO: зарегистрируйте необходимые маршруты
]
