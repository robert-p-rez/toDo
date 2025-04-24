from flask import Blueprint, request, redirect, render_template
from services.task_service import task_service

task_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

@task_bp.route("/", methods=["GET"])
def view_tasks():
    tasks = task_service.get_all_tasks()
    return render_template("task_list.html", tasks=tasks)

@task_bp.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    if title:
        task_service.add_task(title)
    return redirect("/tasks/")

@task_bp.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task_service.delete_task(task_id)
    return redirect("/tasks/")
