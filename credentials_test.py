import  unittest
from credentials import  Credentials
import pyperclip


class TestCredentials(unittest.TestCase):
    """Test class that defines test cases for the Credential class behaviours."""

    def setUp(self):
        """setUp method to define instructions that will be executed before each test method."""
        self.new_user_credential=Credentials("email","kibet@gmail.com","Kibbs")

    def tearDown(self):
        """ tearDown method that does clean up after each test case has run."""
        Credentials.use_credentials_list= []

    # First test--check if we can create users
    def test_init(self):
        """test_init test case to test if the object is initialized properly"""
        self.assertEqual(self.new_user_credential.account,"email")
        self.assertEqual(self.new_user_credential.username,"kibet@gmail.com")
        self.assertEqual(self.new_user_credential.password,"Kibbs")

    # Second Test --- check if it can save users
    def test_save_user_credentials(self):
        """test case to test if the if user credintials are saved"""

        self.new_user_credential.save_credentials()
        self.assertEqual(len(Credentials.use_credentials_list), 1)

    # Third Test --- check if it can save multiple users
    def test_save_multiple_user_credentials(self):
        """A test case to check if we can save multiple user credential objects"""
        self.new_user_credential.save_credentials()
        test_user_credentials = Credentials("twitter", "twitter#", "twitter1234")
        test_user_credentials.save_credentials()
        self.assertEqual(len(Credentials.use_credentials_list), 2)

    # Forth test ---check if we can delete users
    def test_delete_user_credentials(self):
        """test_delete_user_credentials to test if we can remove user_credentials from our   use_credentials_list"""
        self.new_user_credential.save_credentials()
        test_user_credentials = Credentials("twitter", "twitter##", "twitter1234")
        test_user_credentials.save_credentials()
        self.new_user_credential.delete_credentials()  # Deleting a user object
        self.assertEqual(len(Credentials.use_credentials_list), 1)

    # Fifth test ---check if user exist
    def test_existance_by_username(self):
        """test to check if we can find a user by username and display information"""

        self.new_user_credential.save_credentials()
        test_user_credentials = Credentials("twitter", "twitter##", "twitter1234")
        test_user_credentials.save_credentials()
        found_username = Credentials.find_by_username("twitter##")
        self.assertEqual(found_username.username, test_user_credentials.username)

    # Sixth test ---check if user exist
    def test_existance_by_password(self):
        """test to check if we can find a user by password and display information"""

        self.new_user_credential.save_credentials()
        test_user_credentials = Credentials("twitter", "twitter##", "twitter1234")
        test_user_credentials.save_credentials()
        found_password = Credentials.find_by_password("twitter1234")
        self.assertEqual(found_password.password, test_user_credentials.password)
