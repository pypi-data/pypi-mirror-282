# tests/test_validator.py

import unittest
from datavalidator.validator import DataValidator

class TestDataValidator(unittest.TestCase):

    def setUp(self):
        self.validator = DataValidator()

    def test_validate_string(self):
        self.assertTrue(self.validator.validate_string("hello", min_length=3))
        self.assertFalse(self.validator.validate_string("", min_length=1))
        self.assertTrue(self.validator.validate_string("hello", max_length=10))
        self.assertFalse(self.validator.validate_string("hello world", max_length=5))
        self.assertTrue(self.validator.validate_string("abc123", pattern=r'^[a-z0-9]+$'))
        self.assertFalse(self.validator.validate_string("abc-123", pattern=r'^[a-z0-9]+$'))

    def test_validate_number(self):
        self.assertTrue(self.validator.validate_number(5, min_value=1, max_value=10))
        self.assertFalse(self.validator.validate_number(-5, positive=True))
        self.assertTrue(self.validator.validate_number(-5, negative=True))
        self.assertFalse(self.validator.validate_number(0, positive=True))
        self.assertTrue(self.validator.validate_number(0, negative=False))
        self.assertTrue(self.validator.validate_number(5, integer=True))
        self.assertFalse(self.validator.validate_number(5.5, integer=True))

    def test_validate_email(self):
        self.assertTrue(self.validator.validate_email("example@example.com"))
        self.assertFalse(self.validator.validate_email("invalid-email"))

    def test_validate_date(self):
        self.assertTrue(self.validator.validate_date("2024-06-30", date_format="%Y-%m-%d"))
        self.assertFalse(self.validator.validate_date("30-06-2024", date_format="%Y-%m-%d"))

    def test_validate_list(self):
        self.assertTrue(self.validator.validate_list([1, 2, 3], min_length=1, element_type=int))
        self.assertFalse(self.validator.validate_list([], min_length=1))
        self.assertTrue(self.validator.validate_list([1, 2, 3], max_length=5))
        self.assertFalse(self.validator.validate_list([1, 2, 3], max_length=2))
        self.assertTrue(self.validator.validate_list([1, 2, 3], element_type=int))
        self.assertFalse(self.validator.validate_list([1, '2', 3], element_type=int))

    def test_validate_dict(self):
        data = {"name": "Alice", "age": 30}
        self.assertTrue(self.validator.validate_dict(data, required_keys=["name", "age"], key_types={"name": str, "age": int}))
        self.assertFalse(self.validator.validate_dict(data, required_keys=["name", "email"]))
        self.assertFalse(self.validator.validate_dict(data, key_types={"name": int}))

if __name__ == "__main__":
    unittest.main()
