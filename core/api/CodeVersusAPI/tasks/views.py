from django.shortcuts import render
from django.forms import model_to_dict

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all().values()
        return Response({"tasks": TaskSerializer(tasks, many=True).data, "count": len(tasks)})

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_task = Task.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            level=request.data["level"],
            time_complexity=request.data["time_complexity"],
            space_complexity=request.data["space_complexity"],

        )
        return Response(model_to_dict(new_task))


# class TaskAPIView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
