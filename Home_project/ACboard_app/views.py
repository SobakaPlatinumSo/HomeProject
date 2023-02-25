from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from .models import Air_Condition, AirCondition
from .serializers import AirConditionRequest
from django.http import HttpResponse


def AirConditionViews(request):
	serializer = AirConditionRequest(Air_Condition)
	json = JSONRenderer().render(serializer.data)
	response = json
	return 	HttpResponse(response)
