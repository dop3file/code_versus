import Pyro4

from test_storage import TestStorage
from test_system import Task


test_storage = TestStorage()


@Pyro4.expose
class TaskExecutor:
    def solve(self, task_id: str | int, code: str, time_limit: int):
        tests = test_storage.get_tests_from_task(task_id=int(task_id))
        task = Task(tests, time_limit)
        task.run_tests(code)
        result = [task.count_failed_tests == 0]
        result.extend([test.__dict__ for test in task.tests])
        return result


daemon = Pyro4.Daemon()
uri = daemon.register(TaskExecutor)

print(uri)
daemon.requestLoop()
