from his_functions import check_file, create_file, add_pwd

save_pwd = ""

def save_pwd(user_pwd):
    while True:
        # User input - save password?
        save_pwd = input("Do you want to save this password? Yes or No: ")
        # Yes - Does password file exist?
        if save_pwd == "Yes" or save_pwd == "yes":
            # Yes - password file exists
            try:
                check_file()
                add_pwd(str(user_pwd))
                print(f"I have saved your password - {user_pwd}.")
                break
            # No - password file does not exist, create a file.
            except FileNotFoundError:
                create_file()
                add_pwd(user_pwd)
                break
        elif save_pwd == "No" or save_pwd == "no":
            print("I have not saved your password.")
            break
        else:
            print("Sorry, I didn't quite get that. Do you want to save this password? Please enter 'Yes' or 'No'.")
            continue


           
                
                    # Yes - append password file
                    # No - create and write to password file
                # No - re-prompt user for action