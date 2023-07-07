import subprocess
import time
import threading
from typing import List


from utils import TooLongTest
from test_storage import TestStorage


class Task:
    def __init__(self, tests: list, max_exec_time: int) -> None:
        self.tests = tests
        self.max_exec_time = max_exec_time
        self.count_success_tests = 0
        self.count_failed_tests = 0

    def run_test(self, code: str, test):
        command = ["python3", "-c", code]
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, universal_newlines=True)
        try:
            time_before = time.time()
            stdout, stderr = process.communicate(input=test.input_data)
            test.total_exec_time = (time.time() - time_before) / 1000

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
        threads = []
        for i in range(len(self.tests)):
            thread = threading.Thread(target=self.run_test, args=(code, self.tests[i]))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def get_avg_exec_time(self) -> float:
        return sum([test.total_exec_time for test in self.tests]) / len(self.tests)


if __name__ == "__main__":

    tests = test_storage.get_tests_from_task(task_id=1)
    task = Task(tests, 1)
    code_sample = """
x = input().split(' ')
result = ''

for word in x[::-1]:
    result += f'{word} '
print(result[:-1])
    """
    before = time.time()
    task.run_tests(code_sample)
    print(time.time() - before)
    print(task.get_avg_exec_time())
