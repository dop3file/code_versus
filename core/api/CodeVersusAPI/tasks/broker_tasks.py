import Pyro4
from .models import TestGroup, Test, Task
from users.models import CustomUser
from django.core import serializers
from .serializers import TestSerializer
from rest_framework.renderers import JSONRenderer


uri = "PYRO:obj_f7c4de90ac794278852b121dc639093e@localhost:65316"
task_executor = Pyro4.Proxy(uri)


def solve_task(user: CustomUser, task_id: int, code: str, time_complexity: int):
    result = task_executor.solve(task_id, code, time_complexity)
    current_task = Task.objects.get(pk=task_id)
    test_group = TestGroup(
        status=result[0],
        user=user,
        task=current_task
    )
    test_group.save()
    tests = []
    for test in result[1:]:
        test = Test(
            status=test["status"],
            task_group=test_group,
            details=test["report"] if test["report"] else "ok",
            time_complexity=test["total_exec_time"],
            space_complexity=0
        )
        test.save()
        tests.append(test)
    serializer = TestSerializer(tests, many=True)
    return serializer.data