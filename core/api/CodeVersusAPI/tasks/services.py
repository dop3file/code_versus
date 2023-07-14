from rest_framework.views import exception_handler
from rest_framework.response import Response

from .models import Task, Test
from .serializers import TestSerializer
from .broker_tasks import solve_task, add_test
from users.models import CustomUser
from .models import TestGroup
from CodeVersusAPI.exceptions import NotFoundException


class TaskService:
    def solve(self, user: CustomUser, task_id: int, code: str):
        try:
            current_task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            raise NotFoundException
        return solve_task(user, task_id, code, current_task.time_complexity)

    def get_details(self, user: CustomUser, test_group_id: int):
        try:
            test_group = TestGroup.objects.get(pk=test_group_id, user=user)
        except TestGroup.DoesNotExist:
            raise NotFoundException
        tests = Test.objects.filter(test_group=test_group)
        serializer = TestSerializer(tests, many=True)
        return serializer.data