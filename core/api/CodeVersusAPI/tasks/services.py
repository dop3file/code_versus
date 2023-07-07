from rest_framework.views import exception_handler
from rest_framework.response import Response

from .models import Task, Test
from CodeVersusAPI.exceptions import ServiceException
from .broker_tasks import solve_task
from users.models import CustomUser


class TaskService:
    def solve(self, user: CustomUser, task_id: int, code: str):
        current_task = Task.objects.get(pk=task_id)
        return solve_task(user, task_id, code, current_task.time_complexity)

    def get_test_details(self):
        ...