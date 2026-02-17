import json
import os


status_list = ["Pending", "In Progress", "Complete", "Cancelled"]
priority_list = [i for i in range(6)]


def load_from_file(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = {}
    return tasks


def add_task(tasks):
    if not tasks:
        task_id = 1
    else:
        task_id = max(int(task_id) for task_id in tasks.keys()) + 1
    title = input("Enter Task name: ")
    description = input("Enter Task discription: ")
    print("Choose status: ")
    for index , status in enumerate(status_list):
        print(f"{index + 1} - {status}")
    while True:
        try:
            status_option = int(input("Enter the status number:"))
            status = status_list[status_option - 1]
            break
        except ValueError:
            print("invalid input please try again!")
        except IndexError:
            print(f"Please enter a number between 1 and {len(status_list)}")
    try:
        priority = int(input("Enter priority from 0 to 5: "))
    except ValueError:
        print("invalid input please try again!")
    if status in status_list and priority in priority_list:
        tasks[task_id] = {
            "title": title,
            "description": description,
            "status": status,
            "priority": priority,
        }
        print("Task {} added successfully".format(title))
    else:
        print("Can't be added the priority/status is out of range")
    return tasks


def display_tasks(tasks):
    print("All tasks: ")
    print(json.dumps(tasks, indent=4))
    print("Tasks displayed successfully")


def sort_tasks(tasks):
    sorted_tasks = dict(
        sorted(
            tasks.items(), key=lambda item: item[1]["priority"]
        )
    )
    print(sorted_tasks)
    print("According to the priority tasks sorted successfully")


def mark_done_by_id(tasks):
    task_id = int(input("Enter Task id: "))
    marked = False
    for key in tasks:
        if int(key) == int(task_id):
            tasks[key]["status"] = "Complete"
            marked = True
            print("Task {} marked as done successfully".format(task_id))
            break
    if not marked:
        print("Task id doesn't exist")


def mark_done_by_name(tasks):
    task_title = input("Enter Task name: ")
    marked = False
    for key in tasks:
        if tasks[key]["title"] == task_title:
            tasks[key]["status"] = "Complete"
            marked = True
            print("Task {} marked as done successfully".format(task_title))
            break
    if not marked:
        print("Task title doesn't exist")


def change_priority_by_id(tasks):
    task_id = int(input("Enter Task id: "))
    new_priority = int(input("Enter the new priority: "))
    if new_priority in priority_list:
        marked = False
        for key in tasks:
            if int(key) == int(task_id):
                tasks[key]["priority"] = new_priority
                marked = True
                print("Task {} priority changed successfully".format(task_id))
                break
        if not marked:
            print("Task id doesn't exist")
    else:
        print("Task {} can't be updated".format(task_id))
        print("because the new priorty is out of range")


def change_priority_by_name(tasks):
    task_title = input("Enter Task name: ")
    new_priority = int(input("Enter the new priority: "))
    if new_priority in priority_list:
        marked = False
        for key in tasks:
            if tasks[key]["title"] == task_title:
                tasks[key]["priority"] = new_priority
                marked = True
                print("Task {} priority changed successfully".format(task_title))
                break
        if not marked:
            print("Task title doesn't exist")
    else:
        print("Task {} can't be updated".format(task_title))
        print("because the new priorty is out of range")


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
