# T1A3 - Terminal application

# Overview

The Password Generator is an application designed to generate, store, retrieve and delete passwords.

Users can provide their password requirements such as password length and character types. A randomised password will then be generated.

Developed using Python, the Password Generator can be executed directly from the terminal.

**Note:** The below only includes the Help documentation. Please refer to the README document in the assignment submission.

# Help documentation

## Installation

1. Check you meet the hardware and system requirements.
2. Go to [github.com:hotteok219/T1A3-terminalapp](https://github.com/hotteok219/T1A3-terminalapp).
3. Select **<> Code**.
4. Select **Download ZIP**.
A zip file called *T1A3-terminalapp-main.zip* will be downloaded to your local drive.
5. Extract/unzip the zip file.
6. Open a terminal.
> Examples of terminals include: [Terminal (Mac)](https://support.apple.com/en-au/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac), [WSL (Windows)](https://learn.microsoft.com/en-us/windows/wsl/install) or [Ubuntu (Linux)](https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal).
7. In the terminal, navigate to the directory of the extracted zip file. The folder should be named *T1A3-terminalapp-main*.
> **Note:** 
> * Run change directory (`cd`) to navigate to another directory. 
> * Run print working directory (`pwd`) to find out what your current directory is.
> * Run list (`ls`) to print a list of files and folders in your current directory.
> * Visit [Coderbar.io - Introduction to the command line](https://tutorials.codebar.io/command-line/introduction/tutorial.html#:~:text=Example%201%3A%20navigating%20around%20in%20the%20terminal) for some further guidance.
8. To run the application, in the terminal, enter `./run.sh`.

**Note:** An alternate option for steps 4 to 7 is to clone the repository. Follow the steps as detailed by [GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

### What happens next
The application will check that you have Python installed. If Python is installed, it will check for a virtual environment. If this hasn't been created, the application will automatically create and activate it for you. The application will then install any necessary packages. You do not need to do anything until you see the **Main menu** appear.


## Application's dependencies
The application requires all files in the GitHub zip to be available in the same directory. In addition to the Python modules, this also includes:
- requirements.txt
- test/test_pwd_history.csv

The application will need to create a virtual environment named `pwdgen-venv`. Within the virtual environment, external Python packages will be installed.

Packages include (but are not limited to):
* pytest
* colored

For a full list, please review *requirements.txt*

This will automatically be created and installed when you run the program for the first time.

## Hardware and system requirements

* Python (minimum Python 3.10.x)
*Visit [python.org](https://www.python.org/downloads/) for more information.*
* a terminal
*Examples of terminals include: [Terminal (Mac)](https://support.apple.com/en-au/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac), [WSL (Windows)](https://learn.microsoft.com/en-us/windows/wsl/install) or [Ubuntu (Linux)](https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal).*

### Development specifications
The application was developed and tested on the below hardware and system specifications.
* **CPU:** Intel Core i5-6500 @ 3.20GHz, 4 core
* **RAM:** 16.0 GB
* **Operating system:** Windows 10 Pro

## How to run command line arguments

### Main menu

> \*************
>   Main menu
> \*************
> 1. I want to create a new password.
> 2. I want to view my passwords.    
> 3. I want to delete a password.    
> 4. I want to exit.
> 
> Please enter 1, 2, 3 or 4:

Input the number that corresponds with the menu item (`1`, `2`, `3` or `4`).

Press `enter`.

For example: To create a new password, input `1` and press `enter` on the keyboard.

### Create a new password.

> Great! We can create a new password.
> How long should the password be?

Input a number for the length of the password. The number should be 6 or higher.

Press `enter`.

If the number is less than 6, the error `"Your password length is too short. Passwords should be at least 6 characters long."` will appear.

There is also a maximum of 5 invalid attempts before the application will automatically exit.

> Okay, we'll create a password that is \<user input number> characters long.
> What are the password requirements?
> 1. Enter 1 to include lowercase letters - e.g. a, b, c
> 2. Enter 2 to include uppercase letters - e.g. A, B, C
> 3. Enter 3 to include numbers - e.g. 1, 2, 3
> 4. Enter 4 to include special characters - e.g !, @, #
> 5. Enter 5 if there are no more requirements.
> 6. Enter 6 to exit.
>
> Please enter 1, 2, 3, 4, 5 or 6:

Input a number that corresponds with the requirements menu item (`1`, `2`, `3`, `4`, `5` or `6`).

Press `enter`.

For example:
* To include special characters in the requirements, input `4` and press `enter`.
* To exit the app, input `6` and press `enter` on the keyboard.

**Note about entering requirements**

When inputting `1`, `2`, `3`, or `4`, the menu will reappear and additional requirements can be added.

If there are no further requirements, input `5` and press `enter`.

If any requirement selections are duplicated, the application will only consider it once.

### Save a password

> Thanks for providing the requirements. Your password is being generated.
> Your password is: \<generated password>
> Do you want to save this password? Yes or No: 

Enter `Yes` or `No`.

Press `enter`.

If the user chooses to save the password, the following prompt will appear:

> Enter a label for this password (e.g. email, banking): 

Enter a name for the password.

Press `enter`.

The password name cannot be blank, or the following error will appear `"Input cannot be empty."`

### View passwords

> Great! Please see your passwords below:  
> Password ID, Password
> Example, Example password
> Example, Example password
> Example, Example password
> Press enter to go back to the main menu.

View the passwords under the line `"Great! Please see your passwords below:"`.
Once done, press `enter` on the keyboard.

### Delete a password

> Enter the label of the password you want to delete: 

Enter the name of the password that needs to be deleted. (Note: This isn't the actual password).

Press `enter`.

**Note:** If the password doesn't exist, an error will display: `"The password for <password label> doesn't exist."` (`<password label>` represents the label the user has entered.)

### Exit the application

Users can follow the prompts to exit the application.

Alternatively, the use can press `Ctrl` + `C` from their keyboard and the application will exit.
