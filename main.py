from operations import (
    load_from_file,
    add_task,
    display_tasks,
    sort_tasks,
    mark_done_by_id,
    mark_done_by_name,
    change_priority_by_id,
    change_priority_by_name,
    delete_task,
    save_in_file,
)


def main():
    tasks = load_from_file("tasks.json")
    print(tasks)
    global task_id
    status_list = ["Pinding", "In Progress", "Complete", "Cancelled"]
    priority_list = [i for i in range(6)]
    task_id = 0
    while True:
        print("________________________Task Menu________________________")
        print("choose one from Task menu:")
        print("1- Add a Task")
        print("2- View Tasks")
        print("3- Sort Tasks")
        print("4- Mark Task as Done")
        print("5- Change task priority")
        print("6- Delete Task")
        print("7- Exit Program")
        print("8- Save")
        try:
            option = int(input("Enter your option number: "))
            if not option >= 1 and not option <= 8:
                print("Please enter a number between 1 and 8 ")
        except ValueError:
            print("invalid input please try again!")
        match option:
            case 1:
                if not tasks:
                    task_id = 1
                else:
                    task_id = max(int(task_id) for task_id in tasks.keys()) + 1
                title = input("Enter Task name: ")
                discription = input("Enter Task discription: ")
                print("Choose status: ")
                print("1- Pinding")
                print("2- In Progress")
                print("3- Complete")
                print("4- Cancelled")

                try:
                    status_option = int(input("Enter the status number:"))
                    if not status_option >= 1 and not status_option <= 4:
                        print("Please enter a number between 1 and 4 ")
                except ValueError:
                    print("invalid input please try again!")

                if status_option == 1:
                    status = "Pinding"
                elif status_option == 2:
                    status = "In Progress"
                elif status_option == 3:
                    status = "Complete"
                elif status_option == 4:
                    status = "Cancelled"
                else:
                    print(
                        "Task {} can't be added "
                        "the status is out of range".format(title)
                    )
                    continue
                try:
                    priority = int(input("Enter priority from 0 to 5: "))
                except ValueError:
                    print("invalid input please try again!")
                if status in status_list and priority in priority_list:
                    tasks = add_task(
                        tasks, task_id, title, discription, status, priority
                    )
                    print("Task {} added successfully".format(title))
                else:
                    print("Can't be added the priority/status is out of range")
            case 2:
                display_tasks(tasks)
                print("Tasks displayed successfully")
            case 3:
                sort_tasks(tasks)
                print("According to the priority tasks sorted successfully")
            case 4:
                print("Mark Task as done according to:")
                print("1- Task id")
                print("2- Task name")
                try:
                    mark_done_option = int(input("Enter your option: "))
                    if not mark_done_option >= 1 and not mark_done_option <= 2:
                        print("Please enter a number between 1 and 2 ")
                except ValueError:
                    print("invalid input please try again!")
                if mark_done_option == 1:
                    id = int(input("Enter Task id: "))
                    mark_done_by_id(tasks, id)
                elif mark_done_option == 2:
                    title = input("Enter Task name: ")
                    mark_done_by_name(tasks, title)
            case 5:
                print("Change priority according to:")
                print("1- Task id")
                print("2- Task name")
                try:
                    change_priority_option = int(input("Enter your option: "))
                    if (
                        not change_priority_option >= 1
                        and not change_priority_option <= 2
                    ):
                        print("Please enter a number between 1 and 2 ")
                except ValueError:
                    print("invalid input please try again!")
                if change_priority_option == 1:
                    task_id = int(input("Enter Task id: "))
                    new_priority = int(input("Enter the new priority: "))
                    if new_priority in priority_list:
                        change_priority_by_id(tasks, task_id, new_priority)
                    else:
                        print("Task {} can't be updated".format(title))
                        print("because the new priorty is out of range")
                        continue
                elif change_priority_option == 2:
                    title = input("Enter Task name: ")
                    new_priority = int(input("Enter the new priority: "))
                    if new_priority in priority_list:
                        change_priority_by_name(tasks, title, new_priority)
                    else:
                        print("Task {} can't be updated".format(title))
                        print("because the new priorty is out of range")
                        continue
            case 6:
                try:
                    task_id = int(input("Enter Task id: "))
                except ValueError:
                    print("invalid input please try again!")
                delete_task(tasks, task_id)
            case 7:
                return
            case 8:
                save_in_file(tasks)
                print("Tasks saved in tasks file successfully")
            case _:
                return "Invalid option number"


if __name__ == "__main__":
    main()
