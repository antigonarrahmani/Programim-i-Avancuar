# Run: python -m unittest test_validate_user_data.py
import unittest
from validate_user_data import validate_user_data

class TestValidateUserData(unittest.TestCase):
    
    def test_valid_user_data(self):
        user_data = {
            "username": "validUser123",
            "email": "validuser@example.com",
            "password": "Password1!",
            "age": 25,
            "referral_code": "ABCDEFGH"
        }
        result = validate_user_data(user_data)
        self.assertTrue(result["is_valid"])
    
    def test_invalid_email_format(self):
        user_data = {
            "username": "validUser123",
            "email": "invalidemail.com",
            "password": "Password1!",
            "age": 25
        }
        result = validate_user_data(user_data)
        self.assertFalse(result["is_valid"])
        self.assertEqual(result["errors"]["email"], "Invalid email format")
    
    def test_password_too_short(self):
        user_data = {
            "username": "validUser123",
            "email": "validuser@example.com",
            "password": "short",
            "age": 25
        }
        result = validate_user_data(user_data)
        self.assertFalse(result["is_valid"])
        self.assertEqual(result["errors"]["password"], "Password must be at least 8 characters long")
    
    def test_missing_username(self):
        user_data = {
            "email": "validuser@example.com",
            "password": "Password1!",
            "age": 25
        }
        result = validate_user_data(user_data)
        self.assertFalse(result["is_valid"])
        self.assertEqual(result["errors"]["username"], "Username is required")
    
    def test_age_under_18(self):
        user_data = {
            "username": "validUser123",
            "email": "validuser@example.com",
            "password": "Password1!",
            "age": 17
        }
        result = validate_user_data(user_data)
        self.assertFalse(result["is_valid"])
        self.assertEqual(result["errors"]["age"], "User must be at least 18 years old")
    
    def test_referral_code_too_short(self):
        user_data = {
            "username": "validUser123",
            "email": "validuser@example.com",
            "password": "Password1!",
            "referral_code": "ABCD"
        }
        result = validate_user_data(user_data)
        self.assertFalse(result["is_valid"])
        self.assertEqual(result["errors"]["referral_code"], "Referral code must be exactly 8 characters")
    
    def test_valid_referral_code(self):
        user_data = {
            "username": "validUser123",
            "email": "validuser@example.com",
            "password": "Password1!",
            "referral_code": "ABCDEFGH"
        }
        result = validate_user_data(user_data)
        self.assertTrue(result["is_valid"])

if __name__ == "__main__":
    unittest.main()