from random import sample
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from colored import fg, bg, attr
from menu_functions import req_menu, exit_app
from err_functions import err_req, err_plen


# User determines password length.
def set_len():
    plen = 0
    invalid_attempt = 0
    for invalid_attempt in range(5):
        try:
            plen = int(input(f"{bg(0)}{fg(221)}How long should the password be?{attr(0)} "))
            if plen <= 5:
                err_plen("Your password length is too short.", invalid_attempt)
            else:
                print(f"{bg(0)}{fg(221)}Okay, we'll create a password that is {plen} characters long.{attr(0)}")
                return plen
        except ValueError as e:
            err_plen(f"{type(e).__name__}: Please enter a numerical value.", invalid_attempt)
        except KeyboardInterrupt:
            exit_app()
        except Exception as e:
            err_plen(f"{type(e).__name__}: Something unexpected has occurred.", invalid_attempt)
    print(f"{bg(0)}{fg(196)}Too many invalid attempts.{attr(0)}")
    exit_app()


# Define lists for lowercase letters, uppercase letters, numbers and special characters.
list_low = ascii_lowercase
list_upp = ascii_uppercase
list_num = digits
list_sym = punctuation


# User determines password requirements.
def set_req():
    user_req = ""
    preq_list = []
    while user_req != "6":
        user_req = req_menu()
        match user_req:
            case 1:
                preq_list += list_low
                print(f"{bg(0)}{fg(220)}You've added lowercase letters to the list of requirements.{attr(0)}")
            case 2:
                preq_list += list_upp
                print(f"{bg(0)}{fg(220)}You've added uppercase letters to the list of requirements.{attr(0)}")
            case 3:
                preq_list += list_num
                print(f"{bg(0)}{fg(220)}You've added numbers to the list of requirements.{attr(0)}")
            case 4:
                preq_list +=  list_sym
                print(f"{bg(0)}{fg(220)}You've added special characters to the list of requirements.{attr(0)}")
            case 5:
                # No requirements selected
                if preq_list == []:
                    print(f"{bg(0)}{fg(196)}You haven't entered any requirements. Please enter at least one requirement.{attr(0)}")
                    continue
                else:
                    # Remove any duplicates
                    preq_list = list(dict.fromkeys(preq_list))
                    print(f"{bg(0)}{fg(220)}Thanks for providing the requirements. Your password is being generated.{attr(0)}")
                    return preq_list
            case 6:
                exit_app()
            case _:
                err_req(f"Something went wrong.")


# Generate password.
def gen_pwd(pwd_req, pwd_len):
    user_pwd = "".join(sample(pwd_req, pwd_len))
    print(f"{bg(0)}{fg(220)}Your password is: {fg(39)}{user_pwd}{attr(0)}")
    return user_pwd