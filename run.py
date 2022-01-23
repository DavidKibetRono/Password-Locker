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