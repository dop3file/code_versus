from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=256
    )
    description = serializers.CharField()
    level = serializers.CharField(
        max_length=256
    )
    time_complexity = serializers.IntegerField()
    space_complexity = serializers.IntegerField()
