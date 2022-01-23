import unittest
from user import User


class TestUser(unittest.TestCase):
    """Test class that defines test cases for the user class behaviours."""

    def setUp(self):
        """setUp method to define instructions that will be executed before each test method."""
        self.new_user = User("David","David@")

    def tearDown(self):
        """tearDown method that does clean up after each test case has run."""

        User.user_list = []

    # First test--check if we can create users
    def test_init(self):
        """test_init test case to test if the object is initialized properly"""

        self.assertEqual(self.new_user.username,"David")
        self.assertEqual(self.new_user.password,"David@")


    if __name__ == "__main__":
        unittest.main()