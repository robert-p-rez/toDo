from models.task_model import Task

class TaskService:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def add_task(self, title):
        task = Task(id=self.counter, title=title)
        self.tasks.append(task)
        self.counter += 1

    def get_all_tasks(self):
        return self.tasks

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]

task_service = TaskService()
