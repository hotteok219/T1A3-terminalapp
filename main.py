from menu_functions import main_menu
from pwd_functions import set_len, set_req, gen_pwd
from file_functions import check_file, view_file, save_pwd

pwd_filename = "pwd_history.csv"

print("Hello! Welcome to the Password Generator. How can I help?")

user_action = ""

while user_action != "3":
    user_action = main_menu()

    match user_action:
        # Create a new password
        case "1":
            print("Great! We can create a new password.")
            pwd_len = set_len()
            pwd_req = set_req()
            user_pwd = gen_pwd(pwd_req, pwd_len)
            save_pwd(user_pwd)

        # View a password
        case "2":
            try:
                check_file()
                view_file(pwd_filename)
            except FileNotFoundError:
                print("You haven't saved any passwords yet.")
                continue
        
        # Exit
        case "3":
            print("Exiting the Password Generator. Goodbye!")
            continue

        # User entered an invalid input
        case _:
            print("You've entered an invalid option. Please enter 1, 2 or 3")