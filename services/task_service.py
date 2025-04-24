from models.task_model import Task

class TaskService:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def add_task(self, title, priority=4):
        task = Task(id=self.counter, title=title, priority=priority)
        self.tasks.append(task)
        self.counter += 1

    def update_priority(self, task_id, priority):
        for task in self.tasks:
            if task.id == task_id:
                task.priority = priority
                break

    def get_all_tasks(self):
        sorted_tasks = sorted(self.tasks, key=lambda x: x.priority)
        grouped_tasks = {}
        for i in range(1, 5):
            grouped_tasks[i] = [task for task in sorted_tasks if task.priority == i]
        return grouped_tasks

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]

task_service = TaskService()
