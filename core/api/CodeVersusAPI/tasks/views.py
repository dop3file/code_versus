from typing import Iterable

from django.shortcuts import render
from django.forms import model_to_dict

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# class TaskAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         raw_tasks = None
#         if pk is not None:
#             task = Task.objects.get(pk=pk)
#             tasks = TaskSerializer(task).data
#         else:
#             raw_tasks = Task.objects.all().values()
#             tasks = TaskSerializer(raw_tasks, many=True).data
#         return Response({"tasks": tasks, "count": len(raw_tasks) if raw_tasks else 1})
#
#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response(status=404)
#         try:
#             instance = Task.objects.get(pk=pk)
#         except:
#             return Response(status=404)
#
#         serializer = TaskSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response(status=404)
#         try:
#             instance = Task.objects.get(pk=pk)
#             instance_pk = instance.pk
#         except:
#             return Response(status=404)
#
#         instance.delete()
#         return Response(f"delete task {instance_pk}", status=200)

