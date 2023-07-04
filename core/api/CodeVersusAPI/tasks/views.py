from typing import Iterable
from typing import Optional

from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task, TaskLevel
from .serializers import TaskSerializer


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(methods=["post"], detail=True)
    def solve(self, request, pk: Optional[int]):
        if pk is None:
            return Response(status=405)
        print(f"Solve task {pk}")
        return Response({"success": True})
