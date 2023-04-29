from random import sample
from colored import fg, bg, attr
from menu_functions import req_menu, exit_app


# Password length
def set_len():
    plen = 0
    invalid_attempt = 0
    for invalid_attempt in range(5):
        try:
            plen = int(input(f"{bg(0)}{fg(221)}How long should the password be?{attr(0)} "))
            if plen <= 5:
                print(f"{bg(0)}{fg(196)}Your password length is too short. Passwords should be at least 6 characters long.{attr(0)}")
            else:
                print(f"{bg(0)}{fg(221)}Okay, we'll create a password that is {plen} characters long.{attr(0)}")
                return plen
        except ValueError:
            print(f"{bg(0)}{fg(196)}Please enter a numerical value.\nNote: Passwords should be at least 6 characters long.{attr(0)}")
            invalid_attempt += 1
        except Exception as e:
            print(f"{bg(0)}{fg(196)}Something unexpected has occurred. Error code: {e}.\nPlease try again with a numerical value over 5.{attr(0)}")
            invalid_attempt += 1
    print(f"{bg(0)}{fg(196)}Too many invalid attempts.{attr(0)}")
    exit_app()
    

# Define lists for lowercase letters, uppercase letters, numbers and symbols
list_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
list_upp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
list_sym = ["!", "@", "#", "$", "%", "^", "&", "*", "?"]

# Set requirements
def set_req():
    user_req = ""
    preq_list = []
    while user_req != "6":
        user_req = req_menu()
        match user_req:
            case "1":
                preq_list += list_low
            case "2":
                preq_list += list_upp
            case "3":
                preq_list += list_num
            case "4":
                preq_list +=  list_sym
            case "5":
                # No requirements selected
                if preq_list == []:
                    print(f"{bg(0)}{fg(196)}You haven't entered any requirements.{attr(0)}")
                    continue
                else:
                    # Remove any duplicates
                    preq_list = list(dict.fromkeys(preq_list))
                    print(f"{bg(0)}{fg(220)}Thanks for providing the requirements. Your password is being generated.{attr(0)}")
                    return preq_list
            case "6":
                exit_app()
            case _:
                print(f"{bg(0)}{fg(196)}You've entered an invalid option.{attr(0)}{bg(0)} Please enter {fg(2)}1{attr(0)}{bg(0)}, {fg(6)}2{attr(0)}{bg(0)}, {fg(13)}3{attr(0)}{bg(0)}, {fg(129)}4{attr(0)}{bg(0)}, {fg(166)}5{attr(0)}{bg(0)} or {fg(199)}6{attr(0)}{bg(0)}.{attr(0)}")

# Generate password
def gen_pwd(pwd_req, pwd_len):
    user_pwd = "".join(sample(pwd_req, pwd_len))
    print(f"{bg(0)}{fg(220)}Your password is: {fg(39)}{user_pwd}{attr(0)}")
    return user_pwd