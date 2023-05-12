from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    screen = models.ImageField(null=True, upload_to='images/')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensors')