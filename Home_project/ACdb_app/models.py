from django.db import models


class AirCondition(models.Model):
    temperature = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)
    CO2 = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)