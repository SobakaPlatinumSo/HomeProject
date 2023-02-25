from rest_framework import serializers


class AirConditionRequest(serializers.Serializer):
	temperature = serializers.CharField(max_length=100)
	humidity = serializers.CharField(max_length=100)
	CO2= serializers.CharField(max_length=100, required=True)
	created= serializers.DateTimeField()