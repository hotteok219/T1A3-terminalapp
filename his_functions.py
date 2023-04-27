import csv

pwd_filename = "pwd_history.csv"

# Check if password history exists
def check_file():
    pwd_file = open(pwd_filename, "r")
    print("Great! We can view your passwords")
    pwd_file.close()

def create_file():
    pwd_file = open(pwd_filename, "w")
    pwd_file.write("password\n")
    pwd_file.close()
    print("A file to store your password history has been created.")

def add_pwd(user_pwd):
    with open(pwd_filename, "a") as pwd_file:
        writer = csv.writer(pwd_file)
        writer.writerow(user_pwd)
