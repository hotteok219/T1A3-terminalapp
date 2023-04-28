import csv

pwd_filename = "pwd_history.csv"

# Check if password history exists
def check_file():
    pwd_file = open(pwd_filename, "r")
    pwd_file.close()


# Create a file for password history
def create_file():
    pwd_file = open(pwd_filename, "w")
    pwd_file.write("My saved passwords\n")
    pwd_file.close()
    print("A file to store your password history has been created.")


# View password history
def view_file(pwd_filename):
    print("Great! Please see your passwords below:")
    with open(pwd_filename, "r") as pwd_file:
        reader = csv.reader(pwd_file)
        for row in reader:
            print(row[0])


# Ask user if they want to save the password
def save_pwd(user_pwd):
    save_pwd = ""
    while True:
        save_pwd = input("Do you want to save this password? Yes or No: ")
        if save_pwd == "Yes" or save_pwd == "yes":
            try:
                check_file()
                add_pwd(str(user_pwd))
                print(f"I have saved your password - {user_pwd}.")
                break
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


# Add password to password history
def add_pwd(user_pwd):
    with open(pwd_filename, "a") as pwd_file:
        writer = csv.writer(pwd_file)
        writer.writerow([user_pwd])