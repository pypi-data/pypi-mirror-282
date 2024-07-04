from flasgger import swag_from
from flask import request, jsonify

from is3_python_sync_plugin.domain.task_node_and_data import TaskNodeAndData
from is3_python_sync_plugin.domain.task_node_result import TaskNodeResult


class PluginController:
    @staticmethod
    def register_routes(app, processor):
        @app.route('/taskNode/handle/execute', methods=['POST'])
        @swag_from('swagger_config.yml')
        def handle_execute():
            data = request.get_json()
            taskNodeAndData = processor.execute(TaskNodeAndData(**data))
            taskNodeResult = TaskNodeResult(task_id=taskNodeAndData.task_id, prj_id=taskNodeAndData.prj_id,
                                            tenant_id=taskNodeAndData.tenant_id, node_id=taskNodeAndData.node_id,
                                            log_id=taskNodeAndData.log_id,
                                            task_instance_id=taskNodeAndData.task_instance_id)
            return jsonify(taskNodeResult.to_dict())

        @app.route('/test/add/<int:a>/<int:b>', methods=['GET'])
        @swag_from('swagger_config.yml')
        def get_sum(a, b):
            return {"result": a + b}
