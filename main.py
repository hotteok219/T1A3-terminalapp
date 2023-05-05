from colored import fg, bg, attr
from menu_functions import main_menu, exit_app
from pwd_functions import set_len, set_req, gen_pwd
from file_functions import check_file, view_file, save_pwd, del_pwd
from err_functions import err_main


print(f"{bg(0)}{fg(39)}Hello! Welcome to the Password Generator. How can I help?{attr(0)}")
pwd_filename = "pwd_history.csv"
user_action = ""

while user_action != "3":
    user_action = main_menu()
    match user_action:
        # User has chosen to create a new password.
        case 1:
            print(f"{bg(0)}{fg(220)}Great! We can create a new password.{attr(0)}")
            pwd_len = set_len()
            pwd_req = set_req()
            user_pwd = gen_pwd(pwd_req, pwd_len)
            save_pwd(user_pwd, pwd_filename)
        # User has chosen to view passwords.
        case 2:
            try:
                check_file(pwd_filename)
                view_file(pwd_filename)
                input(f"{bg(0)}{fg(221)}Press enter to go back to the main menu.{attr(0)} ")
            except FileNotFoundError:
                print(f"{bg(0)}{fg(196)}You haven't saved any passwords yet.{attr(0)}")
                continue
            except KeyboardInterrupt:
                exit_app()
            except Exception as e:
                err_main(f"{type(e).__name__}: Something went wrong.")
        # User has chosen to delete a password.
        case 3:
            try:
                check_file(pwd_filename)
                del_pwd(pwd_filename)
            except FileNotFoundError:
                print(f"{bg(0)}{fg(196)}You haven't saved any passwords yet.{attr(0)}")
                continue
            except KeyboardInterrupt:
                exit_app()
            except Exception as e:
                err_main(f"{type(e).__name__}: Something went wrong.")
        # User has chosen to exit the application.
        case 4:
            exit_app()
        # User has entered an invalid input.
        case _:
            err_main("Something went wrong.")