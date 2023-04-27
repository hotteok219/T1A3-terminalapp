from menu_functions import main_menu
from len_functions import set_len
from req_functions import set_req
from his_functions import check_file


pwd_filename = "pwd_history.csv"

print("Hello! Welcome to the Password Generator. How can I help?")

user_action = ""

while user_action != "3":
    user_action = main_menu()

    match user_action:
        # User selects: create a new password
        case "1":
            print("Great! We can create a new password")

            # User input - password length
            pwd_len = set_len()

            # User input - password requirements
            user_pwd = set_req(pwd_len)

        # User selects: view a password
        case "2":
            # Does password file exist?
            # Yes - password file exists.
            try:
                check_file()
            # No - password file does not exist, but do not create a file, re-prompt user for action.
            except FileNotFoundError:
                print("You haven't saved any passwords yet.")
                continue
        
        # User selects: exit
        case "3":
            print("Exiting the Password Generator. Goodbye!")
            continue

        # User entered an invalid input
        case _:
            print("You've entered an invalid option. Please enter 1, 2 or 3")