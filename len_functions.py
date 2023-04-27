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