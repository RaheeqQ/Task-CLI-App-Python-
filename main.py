from operations import (
    load_from_file,
    add_task,
    display_tasks,
    sort_tasks,
    mark_as_done,
    change_priority,
    delete_task,
    save_in_file,
)


from handle_exception import (
    handle_inner_option,
    handle_inputs,
)


def main():
    tasks = load_from_file("tasks.json")
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
        option = handle_inputs("Enter your option number: ")
        if option == None:
            return
        match option:
            case 1:
                tasks = add_task(tasks)
            case 2:
                display_tasks(tasks)
            case 3:
                sort_tasks(tasks)
            case 4:
                mark_done_option = handle_inner_option()
                if not mark_done_option == 3:
                    mark_as_done(tasks, mark_done_option)
            case 5:
                change_priority_option = handle_inner_option()
                if not change_priority_option == 3:
                    change_priority(tasks, change_priority_option)
            case 6:
                delete_task(tasks)
            case 7:
                return
            case 8:
                save_in_file(tasks)
            case _:
                print(f"Please enter a number between 1 and 8")


if __name__ == "__main__":
    main()
