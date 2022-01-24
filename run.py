#!/usr/bin/env python3
from rich.console import Console
from user import User
from credentials import Credentials

c=Console()

# Creating User
def create_user(username,password):
    """
    function to create new user
    """
    new_user=User(username,password)
    return new_user


# Saving User
def save_user(user):
    """
 Function to save a new user
    """
    user.save_user()

# Deleting a user
def delete_user():
    """
   Function to delete a user
    """
    User.delete_user()


def check_existing_user(username):  # check if the user exists
    """
    check if user exists
    """
    return User.user_exist(username)


# Finding a user by username
def find_user_by_username(username):
    """
    Function to find a user
    """

    return User.find_user(username)


# Finding a user by password
def check_user_password(username,password):
    """
    Function to find a user
    """
    return User.check_user(username, password)

# Find account to be deleted
def find_account_by_username(name_of_account):
    """ Method to find the existing account depending on the account name input"""

    return Credentials.find_account_name(name_of_account)


def save_credentials(credentials):  # save credentials
    """
    function to save credentials
    """
    credentials.save_credentials()


def create_new_credential(acc_name, acc_username, password):
    """
    function to create a new credential
    """
    new_credential = Credentials(acc_name, acc_username, password)
    return new_credential


def login_user_details(username,password):
    """
    method to allow users to login

    """
    logged_username=Credentials.verification_of_users(username,password)
    return logged_username


# Display credentials
def show_credentials():
    """
    function to show all credentials

    """
    return Credentials.display_user_credentials()


def generate_Locker_Password(pwd_length):
    """
    function to generate password

    """
    new_pwd=Credentials.generateLockerPassword(pwd_length)
    return new_pwd

# My main method
def password_locker():
    """Main Method"""
    while True:
        c.print("Please select one of the option to  proceed.""\n "
              "LA - Login to your account?""\n "
              "RA -  Register a new  account?""\n "
                "EX -  Exit password locker application?""\n ",style='blue')
        abbr = input().lower()
        if abbr == "ra":  # user has selected register option
            c.print("Enter your username .....",style="blue")
            username = input()
            c.print("Enter your password .....",style="blue")
            password = input()

            save_user(create_user(username, password))
            c.print("######################################",style="black on white")
            c.print(f'Congratulations {username} your have successfully created an account',style="bold green")
            c.print("######################################",style="black on white")
            print("\n")

        elif abbr=="la": # user has selected a login option
            c.print("Enter your username ...",style="blue")
            username = input()
            c.print("Enter your password ...",style="blue")
            user_password = input()
            if check_existing_user(username):  # check if user exists
                if check_user_password(username, user_password):   # check if password is correct
                    c.print("######################################",style="white on black")

                    c.print(f"Hello {username}.Welcome To Password Locker Manager",style="green")
                    c.print("######################################",style="white on black")

                    while True:
                        c.print("Select one of the following options to continue: \n ",style="blue")
                        c.print("cc - Create a new credential\n "
                              "vc - View saved credentials\n "
                              "dc- Delete credentials\n "
                              "lt - Logout",style="blue")

                        short_code_abbr = input().lower().strip()
                        if short_code_abbr == "cc": # user creates  new credentials
                            c.print("Enter account name: ",style="blue")
                            acc_name=input()
                            c.print("Enter username of account: ",style="blue")
                            acc_username=input()

                            c.print("Select one of the following on passwords" "\n "
                                    "gp - Generate password..." "\n "
                                    "mp - Enter your own password...\n ",style="blue")

                            selected_option = input().lower().strip()

                            if selected_option == 'mp':
                                password = input("Enter Password:\n ")

                            elif selected_option == 'gp':
                                dictated_password_length = int(input("Enter the length of password you want: "))

                                password = generate_Locker_Password(dictated_password_length)
                                c.print(f"Your password is {password}",style="green")
                            else:
                                c.print("Wrong input selection!!!",style="bold red")
                            save_credentials(create_new_credential(acc_name, acc_username, password))

                            c.print(
                                f"New Credential with account name '{acc_name}' and password '{password}' has been created \n ",style="green")

                        elif short_code_abbr=="vc": # View saved credentials

                            print("All credentials are as follows: ")
                            if show_credentials():
                                for data in show_credentials():
                                    c.print(f'Account: {data.account}, Username: {data.username} and Password: {data.password}',style="black on white")
                            else:
                                c.print("There is no any saved data",style="red")

                        elif short_code_abbr == "dc":  # Deleting credentials
                            c.print("Enter account name to delete: ",style="blue")
                            account_i_want_to_delete=input()
                            if find_account_by_username(account_i_want_to_delete):
                                c.print(f'Account {account_i_want_to_delete} has been successfully deleted',style="bold red")
                            else:
                                c.print(f" Account {account_i_want_to_delete} does not exist!!!",style="red")
                        elif short_code_abbr=="lt":  # Logging out from the application
                            c.print("You have successfully logged out!!!",style=" bold white on red")
                            break
                        else:  # no found account
                            c.print("There is no such account!!",style="bold red")
                else:
                    c.print("Invalid password ...please try again", style="red")


            else:
                c.print("Invalid username or password...Please try again",style="red")

        elif abbr == "ex":
            c.print("Thank you for interacting with password locker, bye---.",style="bold yellow")
            break
        else:
            c.print("Invalid Option ",style="bold yellow")


if __name__ == "__main__":
    password_locker()


