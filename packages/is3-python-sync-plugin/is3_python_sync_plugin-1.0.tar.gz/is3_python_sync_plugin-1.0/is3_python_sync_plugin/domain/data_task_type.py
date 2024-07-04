from enum import Enum


class DataTaskType(Enum):
    DYNAMIC = (1, "实时触发")
    SCHEDULE = (2, "定时触发")
    EVENT = (3, "条件触发")

    def __init__(self, code: int, info: str):
        self.code = code
        self.info = info
