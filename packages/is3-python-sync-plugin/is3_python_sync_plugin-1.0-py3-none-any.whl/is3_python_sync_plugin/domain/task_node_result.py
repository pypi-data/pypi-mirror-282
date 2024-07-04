from typing import Optional


class TaskNodeResult:
    def __init__(self, task_id: int, prj_id: int, tenant_id: int, node_id: int, log_id: int,
                 task_instance_id: Optional[str] = None):
        self.task_id = task_id
        self.prj_id = prj_id
        self.tenant_id = tenant_id
        self.node_id = node_id
        self.log_id = log_id
        self.task_instance_id = task_instance_id

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'prj_id': self.prj_id,
            'tenant_id': self.tenant_id,
            'node_id': self.node_id,
            'log_id': self.log_id,
            'task_instance_id': self.task_instance_id,
        }
