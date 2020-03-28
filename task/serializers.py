from rest_framework import serializers
from task.models import *

class activity_periods_serializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%b %d %Y %I:%M%p")
    end_time = serializers.DateTimeField(format="%b %d %Y %I:%M%p")

    class Meta:
        model=activity_periods
        fields='__all__'

class User_serializer(serializers.ModelSerializer):
    activity_periods=activity_periods_serializer(many=True,read_only=True)
    class Meta:
        model=User
        fields='__all__'


