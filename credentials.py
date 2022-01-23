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