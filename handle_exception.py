def handle_inner_option():
    while True:
        print("Choose one:")
        print("1- Task id")
        print("2- Task name")
        print("3- Back to menu")
        try:
            option = int(input("Enter your option: "))
            if not option >= 1 and not option <= 3:
                print("Please enter a number between 1 and 3 ")
                print("--------------------------------------")
            else:
                break
        except ValueError:
            print(f"Invalid input please try again!")
    return option

def handle_inputs(prompt):
    for i in range (3):
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print(f"Invalid input please try again! (you have {2-i} attempts)")
    return None