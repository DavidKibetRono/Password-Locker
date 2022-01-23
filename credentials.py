import string
import random
import pyperclip


class Credentials:
    """Class that generates new instances of credentials"""
    use_credentials_list=[]

    def __init__(self,account,username,password):
        self.account=account
        self.username=username
        self.password=password

    def save_credentials(self):
        """save_credentials method to save save_credentials objects into use_credentials_list """
        Credentials.use_credentials_list.append(self)

    def delete_credentials(self):
        """delete_credentials method deletes saved delete_credentials  from the use_credentials_list"""
        Credentials.use_credentials_list.remove(self)

    # search by username
    @classmethod
    def find_by_username(cls, username):
        """Method that takes in a username and returns a user that matches that username."""

        for user_cred in cls.use_credentials_list:
            if user_cred.username == username:
                return user_cred

    # search by password
    @classmethod
    def find_by_password(cls, password):
        """Method that takes in a password and returns a user that matches that password. """

        for user in cls.use_credentials_list:
            if user.password == password:
                return user

        # Check account details by account name

    @classmethod
    def find_account_name(cls, my_account_name):
        """Method that takes in a account_platform and returns a credentials that matches that account_platform."""
        for credentials in cls.use_credentials_list:
            if credentials.account == my_account_name:
                return credentials
        return False

        # Display all credentials

    @classmethod
    def display_user_credentials(cls):
        """method to display all user credentials"""
        return cls.use_credentials_list

    # Verifying login details
    @classmethod
    def verification_of_users(self, username, password):
        """Method to verify user details"""
        our_user_details = ''
        for user in Credentials.use_credentials_list:
            if (user.username == username and user.password == password):
                our_user_details = user.username
                return our_user_details