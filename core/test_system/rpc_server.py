import logging
import sys

import Pyro4

from test_storage import TestStorage
from test_system import Task
from models import Test


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.debug('This will be logged in Docker Compose logs')


test_storage = TestStorage()


@Pyro4.expose
class TaskExecutor:
    def solve(self, task_id: str | int, code: str, time_limit: int) -> dict:
        tests = test_storage.get_tests_from_task(task_id=int(task_id))
        task = Task(tests, time_limit)
        task.run_tests(code)
        result = {
            "status": task.count_failed_tests == 0,
            "result": [test.__dict__ for test in task.tests]
        }
        return result

    def add_test(self, test: dict) -> None:
        test_storage.insert_test(test)


logging.debug('This will be logged in Docker Compose logs')

Pyro4.Daemon.serveSimple({
    TaskExecutor: 'TaskExecutor',
}, host="0.0.0.0", port=9090, ns=False, verbose=True)
