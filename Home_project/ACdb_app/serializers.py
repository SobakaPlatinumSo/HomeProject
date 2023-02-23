from rest_framework import serializers
from .models import AirCondition


class AirConditionSerializer(serializers.ModelSerializer):
	temperature = serializers.CharField()
	humidity = serializers.CharField()
	CO2= serializers.CharField(required=False)
	created= serializers.CharField()
	class Meta:
		model = AirCondition
		fields = ('temperature', 'humidity', 'CO2', 'created')