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
                tasks = add_task(tasks)
            case 2:
                display_tasks(tasks)
            case 3:
                sort_tasks(tasks)
            case 4:
                while True:
                    print("Mark Task as done according to:")
                    print("1- Task id")
                    print("2- Task name")
                    try:
                        mark_done_option = int(input("Enter your option: "))
                        if not mark_done_option == 1 and not mark_done_option == 2:
                            print("Please enter a number between 1 and 2 ")
                            print("--------------------------------------")
                        elif mark_done_option == 1:
                            mark_done_by_id(tasks)
                            break
                        elif mark_done_option == 2:
                            mark_done_by_name(tasks)
                            break
                    except ValueError:
                        print("invalid input please try again!")
                        print("--------------------------------------")
            case 5:
                while True:
                    print("Change priority according to:")
                    print("1- Task id")
                    print("2- Task name")
                    try:
                        change_priority_option = int(input("Enter your option: "))
                        if not change_priority_option == 1 and not change_priority_option == 2:
                            print("Please enter a number between 1 and 2 ")
                            print("--------------------------------------")
                        elif change_priority_option == 1:
                            change_priority_by_id(tasks)
                            break
                        elif change_priority_option == 2:
                            change_priority_by_name(tasks)
                            break
                    except ValueError:
                        print("invalid input please try again!")
                        print("--------------------------------------")
            case 6:
                for i in range (3):
                    try:
                        task_id = int(input("Enter Task id: "))
                        delete_task(tasks, task_id)
                        break
                    except ValueError:
                        if i == 2:
                            print("Invalid !")
                        print(f"Invalid input please try again! (you have {2-i} attempts)")
            case 7:
                return
            case 8:
                save_in_file(tasks)
                print("Tasks saved in tasks file successfully")
            case _:
                return "Invalid option number"


if __name__ == "__main__":
    main()
