from abc import ABC, abstractmethod

from is3_python_sync_plugin.domain.task_node_and_data import TaskNodeAndData


# 定义抽象基类
class TaskNodeProcessor(ABC):
    @abstractmethod
    def execute(self, taskNodeAndData: TaskNodeAndData):
        pass
