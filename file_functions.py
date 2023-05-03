import csv
from colored import fg, bg, attr
from menu_functions import exit_app

# Check if password history exists
def check_file(pfile):
    pwd_file = open(pfile, "r")
    pwd_file.close()


# Create a file for password history
def create_file(pfile):
    pwd_file = open(pfile, "w")
    pwd_file.write("Password ID,Password\n")
    pwd_file.close()
    print(f"{bg(0)}{fg(220)}A file to store your password history has been created.{attr(0)}")


# View password history
def view_file(pfile):
    print(f"{bg(0)}{fg(220)}Great! Please see your passwords below:{attr(0)}")
    with open(pfile, "r") as pwd_file:
        reader = csv.reader(pwd_file)
        for row in reader:
            print(f"{row[0]}, {row[1]}")

# Ask user if they want to save the password
def save_pwd(user_pwd, pfile):
    while True:
        save_pwd = input(f"{bg(0)}{fg(221)}Do you want to save this password? Yes or No: {attr(0)}")
        if save_pwd == "Yes" or save_pwd == "yes":
            try:
                check_file(pfile)
                pwd_id = lbl_pwd(user_pwd)
                add_pwd(pwd_id, user_pwd, pfile)
                break
            except FileNotFoundError:
                create_file(pfile)
                pwd_id = lbl_pwd(user_pwd)
                add_pwd(pwd_id, user_pwd, pfile)
                break
        elif save_pwd == "No" or save_pwd == "no":
            print(f"{bg(0)}{fg(220)}I have not saved your password.{attr(0)}")
            break
        else:
            print(f"{bg(0)}{fg(196)}Sorry, I didn't quite get that. {fg(221)}Please enter 'Yes' or 'No'.{attr(0)}")
            continue

# Label password
def lbl_pwd(user_pwd):
    while True:
        try:
            pwd_id = input(f"{bg(0)}{fg(221)}Enter a label for this password (e.g. email, banking): {attr(0)}")
            if pwd_id == "":
                raise ValueError
            else:
                return pwd_id
        except ValueError as e:
            print(f"{bg(0)}{fg(196)}{type(e).__name__}: Please provide a label for this password.{attr(0)}")
        except KeyboardInterrupt:
            exit_app()
        except Exception as e:
            print(f"{bg(0)}{fg(196)}{type(e).__name__}: Something unexpected has occurred.{attr(0)}")


# Add password to password history
def add_pwd(pwd_id, user_pwd, pfile):
    with open(pfile, "a") as pwd_file:
        writer = csv.writer(pwd_file)
        writer.writerow([pwd_id, user_pwd])
        print(f"{bg(0)}{fg(220)}I have saved your password - {fg(39)}{user_pwd}{fg(220)} under {fg(39)}{pwd_id}{fg(220)}.{attr(0)}")

# Remove password from password history
def del_pwd(pfile):
    pwd_exists = False
    del_pwdid = input(f"{bg(0)}{fg(221)}Enter the label of the password you want to delete: {attr(0)}")
    del_pwdlist = []

    pwd_exists = chk_pwd(del_pwdid, pfile)
    
    if pwd_exists:
        with open(pfile, "r") as pwd_file:
            reader = csv.reader(pwd_file)
            for row in reader:
                if del_pwdid != row[0]:
                    del_pwdlist.append(row)
                else:
                    print(f"{bg(0)}{fg(220)}Your password for {fg(39)}{del_pwdid}{attr(0)}{bg(0)}{fg(220)} will be deleted.{attr(0)}")
        with open(pfile, "w") as pwd_file:
            writer = csv.writer(pwd_file)
            writer.writerows(del_pwdlist)
    else:
        print(f"{bg(0)}{fg(196)}The password for {fg(39)}{del_pwdid}{attr(0)}{bg(0)}{fg(196)} doesn't exist.{attr(0)}")
        return

# Check password exists in password history
def chk_pwd(pwd, pfile):
    with open(pfile, "r") as pwd_file:
        reader = csv.reader(pwd_file)
        for row in reader:
            if (pwd == row[0]):
                pwd_exists = True
                break
            else:
                pwd_exists = False
    return pwd_exists