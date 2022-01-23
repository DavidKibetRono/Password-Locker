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

