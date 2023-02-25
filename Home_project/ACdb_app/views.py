from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import AirCondition
from .serializers import AirConditionSerializer


class AirConditionDBView(ReadOnlyModelViewSet):
	queryset = AirCondition.objects.all()
	serializer_class = AirConditionSerializer