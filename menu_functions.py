from colored import fg, bg, attr

# Main menu
def main_menu():
    print(f"*************\n  Main menu\n*************")
    print(f"{fg(2)}{bg(0)}1.{attr(0)} I want to create a new password.")
    print(f"{fg(6)}{bg(0)}2.{attr(0)} I want to view my passwords.")
    print(f"{fg(13)}{bg(0)}3.{attr(0)} I want to exit.")
    inp = input(f"Please enter {fg(2)}{bg(0)}1{attr(0)}, {fg(6)}{bg(0)}2{attr(0)} or {fg(13)}{bg(0)}3{attr(0)}: ")
    return inp

# Password requirements menu
def req_menu():
    print(f"{bg(0)}{fg(221)}What are the password requirements?{attr(0)}")
    print(f"{fg(2)}{bg(0)}1.{attr(0)} Enter 1 to include lowercase letters - e.g. a, b, c")
    print(f"{fg(6)}{bg(0)}2.{attr(0)} Enter 2 to include uppercase letters - e.g. A, B, C")
    print(f"{fg(13)}{bg(0)}3.{attr(0)} Enter 3 to include numbers - e.g. 1, 2, 3")
    print(f"{fg(129)}{bg(0)}4.{attr(0)} Enter 4 to include special characters - e.g !, @, #")
    print(f"{fg(166)}{bg(0)}5.{attr(0)} Enter 5 to if there are no more requirements.")
    print(f"{fg(199)}{bg(0)}6.{attr(0)} Enter 6 to exit.")
    req = input(f"{bg(0)}{fg(221)}Enter your requirement: {attr(0)}")
    return req

def exit_app():
    print(f"{bg(0)}{fg(39)}Exiting the Password Generator. Goodbye!{attr(0)}")
    quit()