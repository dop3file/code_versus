from typing import Dict
from dataclasses import dataclass
from pymongo import MongoClient


@dataclass
class TestStorage:
    input_data: str
    output_data: str
    task_id: int


class TestStorage:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["tests"]
        self.collection = self.db['series']

    def insert_test(self, test: Dict[str, str]) -> str:
        return self.collection.insert_one(test).inserted_id