from typing import Dict, List

from pymongo import MongoClient

from models import Test


class TestStorage:
    def __init__(self):
        print(1)
        self.client = MongoClient("mongodb://mongo:27017/")
        self.db = self.client["tests"]
        self.collection = self.db["series"]

    def insert_test(self, test: Dict[str, str]) -> str:
        return self.collection.insert_one(test).inserted_id

    def get_tests_from_task(self, task_id: int) -> List[Test]:
        tests = self.collection.find({"task_id": task_id})
        return [Test(**test) for test in tests]
