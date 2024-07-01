# datavalidator/validator.py

import re
from datetime import datetime

class DataValidator:
    def validate_string(self, value, min_length=0, max_length=None, pattern=None):
        if not isinstance(value, str) or len(value) < min_length:
            return False
        if max_length is not None and len(value) > max_length:
            return False
        if pattern and not re.match(pattern, value):
            return False
        return True

    def validate_number(self, value, min_value=None, max_value=None, integer=False, positive=False, negative=False):
        if not isinstance(value, (int, float)):
            return False
        if integer and not isinstance(value, int):
            return False
        if positive and value <= 0:
            return False
        if negative and value >= 0:
            return False
        if min_value is not None and value < min_value:
            return False
        if max_value is not None and value > max_value:
            return False
        return True

    def validate_email(self, value):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return self.validate_string(value, pattern=pattern)

    def validate_date(self, value, date_format="%Y-%m-%d"):
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            return False

    def validate_list(self, value, min_length=0, max_length=None, element_type=None):
        if not isinstance(value, list) or len(value) < min_length:
            return False
        if max_length is not None and len(value) > max_length:
            return False
        if element_type and not all(isinstance(elem, element_type) for elem in value):
            return False
        return True

    def validate_dict(self, value, required_keys=None, key_types=None):
        if not isinstance(value, dict):
            return False
        if required_keys and not all(key in value for key in required_keys):
            return False
        if key_types:
            for key, key_type in key_types.items():
                if key in value and not isinstance(value[key], key_type):
                    return False
        return True
