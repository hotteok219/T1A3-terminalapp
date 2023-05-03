import csv
from colored import fg, bg, attr

# Check if password history exists
def check_file(pfile):
    pwd_file = open(pfile, "r")
    pwd_file.close()


# Create a file for password history
def create_file(pfile):
    pwd_file = open(pfile, "w")
    pwd_file.write("My saved passwords\n")
    pwd_file.close()
    print(f"{bg(0)}{fg(220)}A file to store your password history has been created.{attr(0)}")


# View password history
def view_file(pfile):
    print(f"{bg(0)}{fg(220)}Great! {fg(221)}Please see your passwords below:({attr(0)}")
    with open(pfile, "r") as pwd_file:
        reader = csv.reader(pwd_file)
        for row in reader:
            print(row[0])


# Ask user if they want to save the password
def save_pwd(user_pwd, pfile):
    save_pwd = ""
    while True:
        save_pwd = input(f"{bg(0)}{fg(221)}Do you want to save this password? Yes or No: {attr(0)}")
        if save_pwd == "Yes" or save_pwd == "yes":
            try:
                check_file(pfile)
                add_pwd(user_pwd, pfile)
                break
            except FileNotFoundError:
                create_file(pfile)
                add_pwd(user_pwd, pfile)
                break
        elif save_pwd == "No" or save_pwd == "no":
            print(f"{bg(0)}{fg(220)}I have not saved your password.{attr(0)}")
            break
        else:
            print(f"{bg(0)}{fg(196)}Sorry, I didn't quite get that. {fg(221)}Please enter 'Yes' or 'No'.{attr(0)}")
            continue


# Add password to password history
def add_pwd(user_pwd, pfile):
    with open(pfile, "a") as pwd_file:
        writer = csv.writer(pwd_file)
        writer.writerow([user_pwd])
    print(f"{bg(0)}{fg(220)}I have saved your password - {fg(39)}{user_pwd}{fg(220)}.{attr(0)}")