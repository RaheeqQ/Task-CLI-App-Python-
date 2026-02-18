import json
import os
from handle_exception import (handle_inputs)


status_list = ["Pending", "In Progress", "Complete", "Cancelled"]
priority_list = [i for i in range(6)]


def load_from_file(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as file:
        try:
            tasks = json.load(file)
            tasks = {int(k): v for k, v in tasks.items()}
        except json.JSONDecodeError:
            tasks = {}
    return tasks


def add_task(tasks):
    if not tasks:
        task_id = 1
    else:
        task_id = max(int(task_id) for task_id in tasks.keys()) + 1
    title = input("Enter Task name: ").strip()
    while not title:
        print("Task name can't be empty!")
        title = input("Enter Task name: ").strip()
    description = input("Enter Task discription: ").strip()
    while not description:
        print("Task description can't be empty!")
        description = input("Enter Task description: ").strip()
    print("Choose status: ")
    for index , status in enumerate(status_list):
        print(f"{index + 1} - {status}")
    while True:
        try:
            status_option = handle_inputs("Enter the status number:")
            if status_option == None:
                print("Back to menu")
                return tasks
            status = status_list[status_option - 1]
            break
        except ValueError:
            print("invalid input please try again!")
        except IndexError:
            print(f"Please enter a number between 1 and {len(status_list)}")
    try:
        priority = handle_inputs("Enter priority from 0 to 5: ")
        if status_option == None:
            print("Back to menu")
            return tasks
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
    print(json.dumps(sorted_tasks, indent=4))
    print("According to the priority tasks sorted successfully")


def mark_as_done(tasks, option):
    task = None
    if option == 1:
        task_id = handle_inputs("Enter Task id: ")
        task = tasks.get(task_id)
    elif option == 2:
        task_title = input("Enter Task name: ")
        for t in tasks.values():
            if t["title"] == task_title:
                task = t
                break
    if task:
        task["status"] = "Complete"
        print("Task marked as done successfully")
    else:
        print("Task doesn't exist")


def change_priority(tasks, option):
    new_priority = handle_inputs("Enter the new priority: ")
    if new_priority not in priority_list:
        print("Task can't be updated")
        print("because the new priorty is out of range")
        return
    task = None
    if option == 1:
        task_id = handle_inputs("Enter Task id: ")
        task = tasks.get(task_id)
    elif option == 2:
        task_title = input("Enter Task name: ")
        for t in tasks.values():
            if t["title"] == task_title:
                task = t
                break      
    if task:
        task["priority"] = new_priority
        print("Task priority changed successfully")
    else:
        print("Task doesn't exist")


def delete_task(tasks):
    task_id = handle_inputs("Enter Task id: ")
    task = tasks.get(task_id)
    if task:
        val = tasks.pop(task_id)
        print("Task popped: ", val)
        print("Task {} deleted successfully".format(task_id))
    else:
        print("Task doesn't exist")



def save_in_file(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved in tasks file successfully")