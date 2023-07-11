import Pyro4

from test_storage import TestStorage
from test_system import Task
from models import Test


test_storage = TestStorage()


@Pyro4.expose
class TaskExecutor:
    def solve(self, task_id: str | int, code: str, time_limit: int) -> list[dict]:
        tests = test_storage.get_tests_from_task(task_id=int(task_id))
        task = Task(tests, time_limit)
        task.run_tests(code)
        result = [task.count_failed_tests == 0]
        result.extend([test.__dict__ for test in task.tests])
        return result

    def add_test(self, test: dict) -> None:
        print(test)
        test_storage.insert_test(test)


daemon = Pyro4.Daemon()
task = TaskExecutor()
with Pyro4.locateNS() as ns:
    ns.register("task", daemon.register(task))
daemon.requestLoop()
