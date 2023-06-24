import subprocess
import time
import threading
from dataclasses import dataclass
from typing import List, Optional

from utils import TooLongTest


@dataclass
class Test:
    input_data: str
    output_data: str
    status: bool = False
    report: Optional[str] = None
    total_exec_time: int = 0


class Task:
    def __init__(self, tests: List[Test], max_exec_time: int) -> None:
        self.tests = tests
        self.max_exec_time = max_exec_time
        self.count_success_tests = 0
        self.count_failed_tests = 0

    def run_test(self, test: Test):
        command = ['python3', 'task.py']
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, universal_newlines=True)
        try:
            time_before = time.time()
            stdout, stderr = process.communicate(input=test.input_data)
            test.total_exec_time = time.time() - time_before

            if test.total_exec_time > self.max_exec_time:
                raise TooLongTest
            elif process.returncode == 0 and stdout.encode() == (test.output_data + "\n").encode():
                print("Test Success")
                test.status = True
                self.count_success_tests += 1
            else:
                print("Test Failed")
                test.status = False
                self.count_failed_tests += 1
        except TooLongTest:
            process.kill()
            stdout, stderr = process.communicate()
            test.status = False
            test.report = str(stderr.encode())

    def run_tests(self, code: str) -> None:
        with open("_task.py", "w") as file:
            file.write(code)

        threads = []
        for i in range(len(self.tests)):
            thread = threading.Thread(target=self.run_test, args=(self.tests[i],))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def get_avg_exec_time(self) -> float:
        return sum([test.total_exec_time for test in self.tests]) / len(self.tests)


if __name__ == "__main__":
    tests = [
        Test(
            input_data="1 1 2",
            output_data="False"
        ),
        Test(
            input_data="1 2 3",
            output_data="True"
        ),
    ]
    task = Task(tests, 1)
    code_sample = """
x = list(map(int, input().split(" ")))
items = set()
for el in x:
    if el in items:
        print(False)
        break
    items.add(el)
else:
    print(True)
    """
    before = time.time()
    task.run_tests(code_sample)
    print(time.time() - before)
    print(task.get_avg_exec_time())