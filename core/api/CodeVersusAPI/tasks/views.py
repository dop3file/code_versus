from typing import Iterable
from typing import Optional

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsAdminOrReadOnly
from .services import TaskService


task_service = TaskService()


class TaskPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = TaskPagination

    @action(methods=["post"], detail=True, permission_classes=(IsAuthenticated,))
    def solve(self, request, pk: Optional[int]):
        print(request.user)
        task_service.solve(pk)
        return Response({"result": f"Solve task {pk}"})

    @action(methods=["get"], detail=True, permission_classes=(IsAuthenticated,))
    def details(self, request, pk: Optional[int]):
        if pk is None:
            return Response(status=405)
        return Response({"result": f"Details of test {pk}"})
