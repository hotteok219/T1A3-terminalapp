print("Hello! Welcome to the Password Generator. How can I help?")

pwd_filename = "pwd_history.csv"

# Main menu
def main_menu():
    print("1. I want to create a new password.")
    print("2. I want to view my passwords.")
    print("3. I want to exit.")
    inp = input("Please enter 1, 2 or 3: ")
    return inp

# Password length
def set_len():
    try:
        plen = int(input("How long should the password be? "))
        print(f"Okay, we'll create a password that is {plen} characters long.")
    except ValueError:
        print("Please enter a numeric character.")

# Password requirements menu
def req_menu():
     print("What are the password requirements?")
     print("1. Enter 1 to include lowercase letters - e.g. a, b, c")
     print("2. Enter 2 to include uppercase letters - e.g. A, B, C")
     print("3. Enter 3 to include numbers - e.g. 1, 2, 3")
     print("4. Enter 4 to include special characters - e.g !, @, #")
     print("5. Enter 5 to if there are no more requirements.")
     print("6. Enter 6 to go back to the main menu.")
     req = input("Enter your requirement: ")
     return req

user_input = ""

while user_input != "3":
    user_input = main_menu()

    match user_input:
        case "1":
            print("Great! We can create a new password")
            # User input - desired length of password
            pwd_len = set_len()
            # User input - requirements of password (lowercase, uppercase, numbers, special characters)
            user_req = ""
            req_list = []
            while user_req != "6":
                user_req = req_menu()

                match user_req:
                    case "1":
                        req_list.append("1")
                    case "2":
                        req_list.append("2")
                    case "3":
                        req_list.append("3")
                    case "4":
                        req_list.append("4")
                    case "5":
                        if req_list == []:
                            print("You haven't entered any requirements")
                            continue
                        else:
                            print(req_list)
                        # Generate password
                    case "6":
                        continue
                    case _:
                        print("You've entered an invalid option. Please enter 1, 2, 3, 4, 5 or 6.")
            
            # User input - save password?
                # Yes - Does password file exist?
                    # Yes - append password file
                    # No - create and write to password file
                # No - re-prompt user for action

        case "2":
            # Does password file exist?
            try:
                # Yes - view password
                pwd_file = open(pwd_filename, "r")
                print("Great! We can view your passwords")
                pwd_file.close()
            except FileNotFoundError:
                # No - error: password file doesn't exist, re-prompt user for action
                print("You haven't saved any passwords yet.")
                continue
        case "3":
            print("Exiting the Password Generator. Goodbye!")
            continue
        case _:
            print("You've entered an invalid option. Please enter 1, 2 or 3")