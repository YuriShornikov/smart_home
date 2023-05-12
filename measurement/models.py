from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)


class Measurement(models.Model):
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensors')