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

