from rest_framework import serializers

from .models import Task, TaskLevel


class TaskSerializer(serializers.ModelSerializer):
    level = serializers.SlugRelatedField(slug_field='level', queryset=TaskLevel.objects.all())

    class Meta:
        model = Task
        fields = "__all__"
