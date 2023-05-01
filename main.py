from colored import fg, bg, attr
from menu_functions import main_menu, exit_app
from pwd_functions import set_len, set_req, gen_pwd
from file_functions import check_file, view_file, save_pwd

print(f"{bg(0)}{fg(220)}Hello! Welcome to the Password Generator. {fg(221)}How can I help?{attr(0)}")

user_action = ""

while user_action != "3":
    user_action = main_menu()

    match user_action:
        # Create a new password
        case 1:
            print(f"{bg(0)}{fg(220)}Great! We can create a new password.{attr(0)}")
            pwd_len = set_len()
            pwd_req = set_req()
            user_pwd = gen_pwd(pwd_req, pwd_len)
            save_pwd(user_pwd)

        # View a password
        case 2:
            try:
                check_file()
                view_file()
                input(f"{bg(0)}{fg(221)}Press enter to go back to the main menu:{attr(0)} ")
            except FileNotFoundError:
                print(f"{bg(0)}{fg(196)}You haven't saved any passwords yet.{attr(0)}")
                continue
        
        # Exit
        case 3:
            exit_app()

        # User entered an invalid input
        case _:
            print(f"{bg(0)}{fg(196)}Something went wrong. Please enter 1, 2 or 3.{attr(0)}")