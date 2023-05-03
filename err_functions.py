from colored import fg, bg, attr

# Error for Main Menu
def err_main(err_msg):
    print(f"{bg(0)}{fg(196)}{err_msg} Please enter 1, 2, 3 or 4.{attr(0)}")

# Error for Requirements menu
def err_req(err_msg):
    print(f"{bg(0)}{fg(196)}{err_msg} Please enter 1, 2, 3, 4, 5 or 6.{attr(0)}")

# Error for password length
def err_plen(err_msg, inv_num):
    print(f"{bg(0)}{fg(196)}{err_msg} Passwords should be at least 6 characters long.{attr(0)}")
    inv_num += 1
    print(f"{bg(0)}{fg(196)}{5-inv_num} invalid attempts remaining.{attr(0)}")