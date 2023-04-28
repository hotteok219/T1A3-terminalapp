from menu_functions import req_menu
from file_functions import save_pwd
from random import sample

# Password length
def set_len():
    try:
        plen = 0
        while plen <= 5:
            plen = int(input("How long should the password be? "))
            if plen <= 5:
                print("We recommend setting a password greater than 5 characters long.")
            else:
                print(f"Okay, we'll create a password that is {plen} characters long.")
                return plen
    except ValueError:
        print("Please enter a numeric character.")

# Define lists for lowercase letters, uppercase letters, numbers and symbols
list_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
list_upp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
list_sym = ["!", "@", "#", "$", "%", "^", "&", "*", "?"]

# Set requirements
def set_req(pwd_len):
    user_req = ""
    req_list = []
    user_pwd = ""

    while user_req != "6":
        user_req = req_menu()
        match user_req:
            case "1":
                req_list += list_low
            case "2":
                req_list += list_upp
            case "3":
                req_list += list_num
            case "4":
                req_list +=  list_sym
            case "5":
                # No requirements selected
                if req_list == []:
                    print("You haven't entered any requirements")
                    continue
                else:
                    print(req_list)
                    
                    # Remove duplicates
                    req_list = list(dict.fromkeys(req_list))
                    print(req_list)
                    
                    # Generate password
                    pwd_list = sample(req_list, int(pwd_len))
                    print(pwd_list)
                    for char in pwd_list:
                        user_pwd += char
                    print(user_pwd)
                    print(type(user_pwd))

                    # Save password?
                    save_pwd(user_pwd)

                    # Return to main menu
                    return
            case "6":
                continue
            case _:
                print("You've entered an invalid option. Please enter 1, 2, 3, 4, 5 or 6.")
            