"""
This file contains unit tests for the `authenticate` function in auth_service.py.
It covers various login scenarios including valid, invalid, and missing credentials.

Author: Your Name
Date: 07-05-2025
"""

import unittest
from auth_service import authenticate
class TestAuthenticate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Start")
    def setUp(self):
        print("Tesing...",self._testMethodName)
    def tearDown(self):
        print("Completed",self._testMethodName)
    def test_username(self):
        result = authenticate("dhoni","123")
        self.assertEqual(result,"Invalid")
    @classmethod
    def tearDownClass(cls):
        print("All test completed ")
if __name__ =="__main__":
    unittest.main()

#proper format:-
# import unittest
# from auth_service import authenticate


# class TestAuthentication(unittest.TestCase):
#     """Unit tests for the authentication logic"""

#     @classmethod
#     def setUpClass(cls):
#         print("\n🔧 [setUpClass] Starting Authentication Test Suite...\n")

#     def setUp(self):
#         print(f"⚙️ [setUp] Running test: {self._testMethodName}")

#     def tearDown(self):
#         print(f"✅ [tearDown] Completed test: {self._testMethodName}\n")

#     @classmethod
#     def tearDownClass(cls):
#         print("\n🧹 [tearDownClass] Finished Authentication Tests.\n")

#     def test_valid_admin_login(self):
#         """✅ Should authenticate admin with correct credentials"""
#         result = authenticate("admin", "admin123")
#         self.assertEqual(result, "Login success")
#         self.assertIsInstance(result, str)
#         self.assertIn("Login", result)

#     def test_valid_user_login(self):
#         """✅ Should authenticate user with correct credentials"""
#         result = authenticate("john", "johnpass")
#         self.assertEqual(result, "Login success")
#         self.assertTrue(result.startswith("Login"))
#         self.assertIsInstance(result, str)

#     def test_invalid_user(self):
#         """❌ Should fail for unknown username"""
#         result = authenticate("abcd", "alicepwd")
#         self.assertEqual(result, "Invalid credentials")
#         self.assertNotIn("success", result.lower())
#         self.assertIsInstance(result, str)

#     def test_wrong_password(self):
#         """❌ Should fail for valid user but wrong password"""
#         result = authenticate("john", "summa")
#         self.assertEqual(result, "Invalid credentials")
#         self.assertIsNotNone(result)

#     def test_empty_username(self):
#         """🚫 Should fail when username is empty"""
#         result = authenticate("", "summa")
#         self.assertEqual(result, "Missing credentials")
#         self.assertIn("Missing", result)

#     def test_empty_password(self):
#         """🚫 Should fail when password is empty"""
#         result = authenticate("summa", "")
#         self.assertEqual(result, "Missing credentials")
#         self.assertNotEqual(result, "Login success")

#     def test_both_fields_empty(self):
#         """🚫 Should fail when both username and password are empty"""
#         result = authenticate("", "")
#         self.assertEqual(result, "Missing credentials")

#     def test_none_inputs(self):
#         """🚫 Should fail gracefully if None is passed as input"""
#         result = authenticate(None, None)
#         self.assertEqual(result, "Missing credentials")


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
