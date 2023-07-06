from rest_framework.views import exception_handler
from rest_framework.response import Response

from .models import Task, Test
from CodeVersusAPI.exceptions import ServiceException


class TaskService:
    def solve(self, task_id: int):
        raise ServiceException

    def get_test_details(self):
        ...