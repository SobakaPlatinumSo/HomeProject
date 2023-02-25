from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from .models import AirCondition
from .serializers import AirConditionRequest
from django.http import HttpResponse


def AirConditionViews(request):
	with open('F:\Project\HomeProject\Home_project\ACboard_app\CurrentAirCondition.txt', 'r') as f:
		Air_Condition = AirCondition(f.readline().strip(), f.readline())
		serializer = AirConditionRequest(Air_Condition)
		json = JSONRenderer().render(serializer.data)
		response = json
		return 	HttpResponse(response)
