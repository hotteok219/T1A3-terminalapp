# Main menu
def main_menu():
    print("1. I want to create a new password.")
    print("2. I want to view my passwords.")
    print("3. I want to exit.")
    inp = input("Please enter 1, 2 or 3: ")
    return inp

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