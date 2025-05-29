"""
setUpClass(cls): Called once before any tests in the class run.
setUp(self): Called before each test method.
tearDown(self): Called after each test method is executed.
tearDownClass(cls): Called once after all tests in the class are done.

"""

import unittest
from unitTesting import authentication, USERS  # importing from separate file

class TestAuthentication(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\nSetting up class resources...")
        cls.users = USERS  # Load users from the USERS dictionary

    def setUp(self):
        print("Setting up before test...")
        self.username = None
        self.password = None

    def tearDown(self):
        print("Cleaning up after test...")
        self.username = None
        self.password = None

    def test_username(self):
        # Valid login
        self.username = "john"
        self.password = "johnpass"
        self.assertEqual(authentication(self.username, self.password), "logged in")

        # Invalid password
        self.password = ""
        self.assertEqual(authentication(self.username, self.password), "invalid creds")

        # Missing username
        self.username = ""
        self.assertEqual(authentication(self.username, self.password), "missing credentials")

        # Unknown user
        self.username = "dhoni"
        self.password = "somepass"
        self.assertEqual(authentication(self.username, self.password), "invalid creds")
    
    @classmethod
    def tearDownClass(cls):
        print("\nAll test cases completed.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
