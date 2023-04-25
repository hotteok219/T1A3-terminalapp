print("Hello! Welcome to the Password Generator. How can I help?")
user_input = input("1. I want to create a new password.\n2. I want to view my passwords.\n3. I want to exit.\nPlease enter 1, 2 or 3: ")

match user_input:
    case "1":
        print("Great! We can create a new password")
    case "2":
        print("Great! We can view your passwords")
    case "3":
        print("Exiting the Password Generator. Goodbye!")
    case _:
        print("You've entered an invalid option. Please enter 1, 2 or 3")