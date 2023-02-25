from django.db import models

class AirCondition:
    def __init__(self, temperature, humidity, CO2=None, created=None):
        self.temperature = temperature
        self.humidity = humidity
        self.CO2 = CO2
        self.created = created