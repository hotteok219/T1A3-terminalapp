from menu_functions import req_menu
from random import sample
from save_functions import save_pwd

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

                    # return user_pwd # this goes back to the main menu
                    save_pwd(user_pwd)
                    return
                    # save_pwd = input("Do you want to save this password? Yes or No: ")
                    # if save_pwd == "Yes" or save_pwd == "yes":
                    #     print("Your password has been saved.")
                    # elif save_pwd == "No" or save_pwd == "no":
                    #     print("Your password was not saved.")
                    # else:
                    #     print("Your answer is invalid. Please enter 'Yes' or 'No'.")
            case "6":
                continue
            case _:
                print("You've entered an invalid option. Please enter 1, 2, 3, 4, 5 or 6.")
            