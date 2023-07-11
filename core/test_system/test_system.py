import subprocess
import time
import threading
from typing import List
import signal


from utils import TooLongTest
from test_storage import TestStorage


def handler():
    raise TooLongTest


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
            try:
                stdout, stderr = process.communicate(input=test.input_data, timeout=self.max_exec_time)
            except subprocess.TimeoutExpired:
                test.total_exec_time = (time.time() - time_before)
                raise TooLongTest
            test.total_exec_time = (time.time() - time_before)

            stdout, stderr = process.communicate()
            if test.total_exec_time > self.max_exec_time:
                raise TooLongTest

            elif process.returncode == 0 and stdout.encode() == (test.output_data + "\n").encode():
                print("Test Success")
                test.status = True
                test.report = str(stderr.encode()) if str(stderr.encode()) != b"" else str(stdout.encode())
                self.count_success_tests += 1
            else:
                print("Test Failed")
                test.status = False
                test.report = str(stderr.encode()) if str(stderr.encode()) != b"" else str(stdout.encode())
                self.count_failed_tests += 1
        except TooLongTest:
            process.kill()
            stdout, stderr = process.communicate()
            test.status = False
            test.report = str(stderr.encode()) if str(stderr.encode()) != b"" else str(stdout.encode())
            self.count_failed_tests += 1

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