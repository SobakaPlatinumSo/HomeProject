from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import AirCondition
from .serializers import AirConditionSerializer


class AirConditionView(ReadOnlyModelViewSet):
	queryset = AirCondition.objects.all()
	serializer_class = AirConditionSerializer