from typing import List, Dict, Any, Optional

from is3_python_sync_plugin.domain.data_task_type import DataTaskType


class TaskNodeAndData:
    def __init__(self, task_id: int, prj_id: int, tenant_id: int, node_id: int, log_id: int,
                 plugin_data_config: Optional[str] = None, rule_expression: Optional[str] = None,
                 task_instance_id: Optional[int] = None, data: Optional[List[Dict[str, Any]]] = None,
                 task_type: Optional[DataTaskType] = None):
        self.task_id = task_id
        self.prj_id = prj_id
        self.tenant_id = tenant_id
        self.node_id = node_id
        self.log_id = log_id
        self.plugin_data_config = plugin_data_config
        self.rule_expression = rule_expression
        self.task_instance_id = task_instance_id
        self.data = data if data is not None else []
        self.task_type = task_type

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'prj_id': self.prj_id,
            'tenant_id': self.tenant_id,
            'node_id': self.node_id,
            'log_id': self.log_id,
            'plugin_data_config': self.plugin_data_config,
            'rule_expression': self.rule_expression,
            'task_instance_id': self.task_instance_id,
            'data': self.data,
            'task_type': self.task_type.name if self.task_type else None
        }
