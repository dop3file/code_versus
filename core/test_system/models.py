from dataclasses import dataclass
from typing import Optional


@dataclass
class Test:
    """
    Класс для внутреннего представления тестов, последующей передачи API серверу
    """
    task_id: int
    test_id: int
    input_data: str
    output_data: str
    status: bool = False
    report: Optional[str] = None
    total_exec_time: int = 0
    _id: Optional[str] = None
