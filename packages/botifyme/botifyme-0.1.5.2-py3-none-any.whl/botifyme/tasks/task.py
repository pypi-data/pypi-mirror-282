class Task:
    def __init__(self, task_id, task_type, task_status, task_data, task_result):
        self.task_id = task_id
        self.task_type = task_type
        self.task_status = task_status
        self.task_data = task_data
        self.task_result = task_result

    def __str__(self):
        return f"Task {self.task_id}: {self.task_status} - {self.task_type} - {self.task_data} - {self.task_result}"
