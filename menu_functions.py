from colored import fg, bg, attr
from err_functions import err_main, err_req

# Main menu
def main_menu():
    invalid_attempt = 0
    while True:
        try:
            print(f"*************\n  Main menu\n*************")
            print(f"{fg(2)}{bg(0)}1.{attr(0)} I want to create a new password.")
            print(f"{fg(6)}{bg(0)}2.{attr(0)} I want to view my passwords.")
            print(f"{fg(58)}{bg(0)}3.{attr(0)} I want to delete a password.")
            print(f"{fg(13)}{bg(0)}4.{attr(0)} I want to exit.")
            inp = int(input(f"Please enter {fg(2)}{bg(0)}1{attr(0)}, {fg(6)}{bg(0)}2{attr(0)}, {fg(58)}{bg(0)}3{attr(0)} or {fg(13)}{bg(0)}4{attr(0)}: "))
            return inp
        except ValueError as e:
            err_main(f"{type(e).__name__}: You've entered an invalid option.")
        except KeyboardInterrupt:
            exit_app()
        except Exception as e:
            err_main(f"{type(e).__name__}: Something went wrong.")


# Password requirements menu
def req_menu():
    while True:
        try:
            print(f"{bg(0)}{fg(221)}What are the password requirements?{attr(0)}")
            print(f"{fg(2)}{bg(0)}1.{attr(0)} Enter 1 to include lowercase letters - e.g. a, b, c")
            print(f"{fg(6)}{bg(0)}2.{attr(0)} Enter 2 to include uppercase letters - e.g. A, B, C")
            print(f"{fg(13)}{bg(0)}3.{attr(0)} Enter 3 to include numbers - e.g. 1, 2, 3")
            print(f"{fg(129)}{bg(0)}4.{attr(0)} Enter 4 to include special characters - e.g !, @, #")
            print(f"{fg(166)}{bg(0)}5.{attr(0)} Enter 5 to if there are no more requirements.")
            print(f"{fg(199)}{bg(0)}6.{attr(0)} Enter 6 to exit.")
            req = int(input(f"Please enter {fg(2)}{bg(0)}1{attr(0)}, {fg(6)}{bg(0)}2{attr(0)}, {fg(13)}{bg(0)}3{attr(0)}, {fg(129)}{bg(0)}4{attr(0)}, {fg(166)}{bg(0)}5{attr(0)} or {fg(199)}{bg(0)}6{attr(0)}: "))
            return req
        except ValueError as e:
            err_req(f"{type(e).__name__}: You've entered an invalid option.")
        except KeyboardInterrupt:
            exit_app()
        except Exception as e:
            err_req(f"{type(e).__name__}: Something went wrong.")

def exit_app():
    print(f"{bg(0)}{fg(39)}Exiting the Password Generator. Goodbye!{attr(0)}")
    quit()