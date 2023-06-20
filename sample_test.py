import subprocess
import signal
import time
import threading
from dataclasses import dataclass


@dataclass
class Test:
    input_data: str
    output_data: str
    status: bool = False
    report: str | None = None
    total_exec_time: int = 0


class Task:
    def __init__(self, tests: list[Test], max_exec_time: int) -> None:
        self.tests = tests
        self.max_exec_time = max_exec_time
        self.count_success_tests = 0
        self.count_failed_tests = 0

    def run_test_sync(self, code):
        with open("task.py", "w") as file:
            file.write(code)
        for test in self.tests:
            self.run_test(test)

    def run_tests(self, code: str):
        with open("task.py", "w") as file:
            file.write(code)

        threads = []
        for i in range(len(self.tests)):
            thread = threading.Thread(target=self.run_test, args=(self.tests[i],))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def run_test(self, test: Test):
        command = ['python3', 'task.py']
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        try:
            signal.alarm(self.max_exec_time)
            time_before = time.time()
            stdout, stderr = process.communicate(input=test.input_data)
            test.total_exec_time = time.time() - time_before
            if process.returncode != 0:
                print(stderr.encode())
            elif process.returncode == 0 and stdout.encode() == (test.output_data + "\n").encode():
                print("Тест пройден!")
                test.status = True
                self.count_success_tests += 1
            else:
                print("Тест провален!")
                test.status = False
                self.count_failed_tests += 1
            signal.alarm(0)
        except TimeoutError:
            process.kill()
            stdout, stderr = process.communicate()
            test.status = False
            test.report = str(stderr.encode())
            print(test.report)


if __name__ == "__main__":
    tests = [
        Test(
            input_data="ovo",
            output_data="True"
        ),
        Test(
            input_data="ovv",
            output_data="False"
        ),
    ]
    task = Task(tests, 1)
    code_sample = """
x = input()
if x == x[::-1]:
    print(True)
else:
    print(False)
    """
    task.run_tests(code_sample)
    print(task.count_success_tests)