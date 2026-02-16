import json
import os


def load_from_file(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = {}
    return tasks


def add_task(tasks, task_id, title, description, status="Pending", priority=0):
    tasks[task_id] = {
        "title": title,
        "description": description,
        "status": status,
        "priority": priority,
    }
    return tasks


def display_tasks(tasks):
    print("All tasks: ")
    print(tasks)


def sort_tasks(tasks):
    sorted_tasks = dict(
        sorted(
            tasks.items(), key=lambda item: item[1]["priority"]
        )
    )
    print(sorted_tasks)


def mark_done_by_id(tasks, task_id):
    marked = False
    for key in tasks:
        if int(key) == int(task_id):
            tasks[key]["status"] = "Complete"
            marked = True
            print("Task {} marked as done successfully".format(task_id))
            break
    if not marked:
        print("Task id doesn't exist")


def mark_done_by_name(tasks, task_title):
    marked = False
    for key in tasks:
        if tasks[key]["title"] == task_title:
            tasks[key]["status"] = "Complete"
            marked = True
            print("Task {} marked as done successfully".format(task_title))
            break
    if not marked:
        print("Task title doesn't exist")


def change_priority_by_id(tasks, task_id, new_priority):
    marked = False
    for key in tasks:
        if int(key) == int(task_id):
            tasks[key]["priority"] = new_priority
            marked = True
            print("Task {} priority changed successfully".format(task_id))
            break
    if not marked:
        print("Task id doesn't exist")


def change_priority_by_name(tasks, task_title, new_priority):
    marked = False
    for key in tasks:
        if tasks[key]["title"] == task_title:
            tasks[key]["priority"] = new_priority
            marked = True
            print("Task {} priority changed successfully".format(task_title))
            break
    if not marked:
        print("Task title doesn't exist")


def delete_task(tasks, task_id):
    deleted = False
    for key in tasks:
        if int(key) == int(task_id):
            val = tasks.pop(key)
            print("Value popped: ", val)
            deleted = True
            print("Task {} deleted successfully".format(task_id))
            break
    if not deleted:
        print("Task title doesn't exist")


def save_in_file(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
