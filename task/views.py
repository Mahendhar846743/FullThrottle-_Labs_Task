from rest_framework.viewsets import ModelViewSet
from task.serializers import *
from task.models import *

class activity_periodsviewset(ModelViewSet):
    queryset = activity_periods.objects.all()
    serializer_class = activity_periods_serializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_serializer


