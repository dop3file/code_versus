from typing import Iterable
from typing import Optional

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination

from .models import Task
from .serializers import TaskSerializer, TestInSerializer
from CodeVersusAPI.permissions import IsAdminOrReadOnly, IsAuthCustom
from .services import TaskService
from .broker_tasks import add_test



class TaskPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = TaskPagination

    @action(methods=["post"], detail=True, permission_classes=(IsAuthCustom,))
    def solve(self, request, pk: Optional[int]):
        code = request.data.get("code")
        return Response(TaskService.solve(request.user, pk, code))

    @action(methods=["get"], detail=True, permission_classes=(IsAuthCustom,))
    def details(self, request, pk: Optional[int]):
        return Response(TaskService.get_details(request.user, pk))

    @action(methods=["post"], detail=False, permission_classes=(IsAdminUser,))
    def test(self, request):
        test_serializer = TestInSerializer(data=request.data)
        test_serializer.is_valid(raise_exception=True)
        add_test(test_serializer.validated_data)
        return Response("ok")
