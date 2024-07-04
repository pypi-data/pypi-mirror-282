import json

import requests

from ..domain.task_node_and_data import TaskNodeAndData


def invoke_plugin_log(msg, taskNodeAndData: TaskNodeAndData, serverName, headers):
    url = "http://118.195.242.175:31900/is3-modules-job/task/log/plugin/log"  # 替换为实际的IP地址和路径
    try:
        message = {"message": msg, "prjId": taskNodeAndData.prj_id, "pluginCode": serverName,
                   "logId": taskNodeAndData.log_id, "taskId": taskNodeAndData.task_id,
                   "nodeId": taskNodeAndData.node_id}
        # 将 message 对象转换为 JSON 字符串
        response = requests.post(url, data=json.dumps(message), headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
