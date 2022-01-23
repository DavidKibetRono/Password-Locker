class User:
    """Class that generates new instances of users"""

    user_list=[]

    def __init__(self, username,password):
        """Initialize the user."""

        self.username = username
        self.password = password

    def save_user(self):
        """save_user method to save user objects into user_list"""

        User.user_list.append(self)

    def delete_user(self):
        """delete_user method deletes saved user  from the user_list"""

        User.user_list.remove(self)

    @classmethod
    def find_user(cls, username):
        """Find user by username"""
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls, username):
        """method to check if user exists"""
        for user in cls.user_list:
            if user.username == username:
                return True
        return False

    @classmethod
    def check_user(cls, username, password):
        """Check if user exists and if password is correct"""
        user = cls.find_user(username)
        if user and user.password == password:
            return True
        return False

    # method to display all users
    @classmethod
    def display_users(cls):
        """method to return all users"""
        return cls.user_list
