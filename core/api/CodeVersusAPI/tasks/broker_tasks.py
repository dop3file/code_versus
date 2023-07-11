import Pyro4

from .models import TestGroup, Test, Task
from users.models import CustomUser
from .serializers import TestSerializer, TestGroupSerializer
from CodeVersusAPI.settings import BROKER_URI


broker_uri = BROKER_URI
task_executor = Pyro4.Proxy(broker_uri)


def solve_task(user: CustomUser, task_id: int, code: str, time_complexity: int):
    result = task_executor.solve(task_id, code, time_complexity)
    current_task = Task.objects.get(pk=task_id)
    test_group = TestGroup(
        status=result[0],
        user=user,
        task=current_task
    )
    test_group.save()
    for test in result[1:]:
        test = Test(
            status=test["status"],
            test_group=test_group,
            details=test["report"] if test["report"] else "ok",
            time_complexity=test["total_exec_time"],
            space_complexity=0
        )
        test.save()
    serializer = TestGroupSerializer(test_group)
    return serializer.data


def add_test(test: dict):
    task_executor.add_test(test)