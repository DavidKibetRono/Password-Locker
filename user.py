class User:
    """Class that generates new instances of users"""

    user_list=[]

    def __init__(self, username,password):
        """Initialize the user."""

        self.username = username
        self.password = password