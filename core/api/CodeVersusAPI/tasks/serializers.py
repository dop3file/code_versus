from rest_framework import serializers

from .models import Task, TaskLevel, Test


class TaskSerializer(serializers.ModelSerializer):
    level = serializers.SlugRelatedField(slug_field='level', queryset=TaskLevel.objects.all())

    class Meta:
        model = Task
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"
