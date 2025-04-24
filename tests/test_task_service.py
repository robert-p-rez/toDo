import pytest
from services.task_service import TaskService

def test_add_and_get_tasks():
    service = TaskService()
    service.add_task("Test Task")
    tasks = service.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Test Task"

def test_delete_task():
    service = TaskService()
    service.add_task("Task to delete")
    service.delete_task(1)
    assert len(service.get_all_tasks()) == 0
