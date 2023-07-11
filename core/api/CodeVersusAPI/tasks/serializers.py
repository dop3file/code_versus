import json

from rest_framework import serializers

from .models import Task, TaskLevel, Test, TestGroup


class TaskSerializer(serializers.ModelSerializer):
    level = serializers.SlugRelatedField(slug_field='level', queryset=TaskLevel.objects.all())

    class Meta:
        model = Task
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class TestGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestGroup
        fields = "__all__"


class TestInSerializer(serializers.BaseSerializer):
    input_data = serializers.CharField()
    output_data = serializers.CharField()
    task_id = serializers.IntegerField()
    test_id = serializers.IntegerField()

    def to_internal_value(self, data):
        mapping = ("input_data", "output_data", "task_id", "test_id")
        result = {}
        for element in mapping:
            element_value = data.get(element)
            if not element_value:
                raise serializers.ValidationError(f"{element} is required")
            result[element] = element_value
        return result