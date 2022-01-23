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