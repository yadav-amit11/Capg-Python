"""
Unit tests for user registration and login functionality using SQLite.
Covers:
- Register new user
- Handle duplicate user
- Missing fields
- Valid and invalid login
"""

import unittest
import os
import sys
os.chdir(r'C:\Users\Administrator\OneDrive\文档\RegEx\user_auth_project')
sys.path.append(os.getcwd())
from auth_core import user_db
from auth_core.user_service import register_user, authenticate_user

class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup the database fresh for testing"""
        user_db.init_db()

    def test_register_new_user(self):
        """Test user registration"""
        result = register_user("alice", "alice123")
        self.assertEqual(result, "User registered")

    def test_register_existing_user(self):
        """Test registration of a duplicate user"""
        result = register_user("alice", "newpass")
        self.assertEqual(result, "User already exists")

    def test_register_with_missing_fields(self):
        """Test registration with empty username or password"""
        self.assertEqual(register_user("", "pass"), "Missing fields")
        self.assertEqual(register_user("user", ""), "Missing fields")

    def test_valid_login(self):
        """Test successful login"""
        result = authenticate_user("alice", "alice123")
        self.assertEqual(result, "Login success")

    def test_invalid_login(self):
        """Test login with wrong password"""
        result = authenticate_user("alice", "wrongpass")
        self.assertEqual(result, "Invalid credentials")

    def test_login_with_missing_credentials(self):
        """Test login with empty username or password"""
        self.assertEqual(authenticate_user("", "pass"), "Missing credentials")
        self.assertEqual(authenticate_user("user", ""), "Missing credentials")


if __name__ == "__main__":
    unittest.main()
