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