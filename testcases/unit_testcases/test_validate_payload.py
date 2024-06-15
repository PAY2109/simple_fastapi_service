import unittest

from utils import validate_payload


class TestValidatePayload(unittest.TestCase):
    def test_validate_payload(self):
        valid_payload = {'date': '31.01.2021', 'periods': 7, 'amount': 10000, 'rate': 6.0}
        is_valid = validate_payload(valid_payload)
        self.assertEqual(True, is_valid)

        invalid_payload = {'date': '31-01-2021', 'periods': 7, 'amount': 10000, 'rate': 6.0}
        is_valid = validate_payload(invalid_payload)
        self.assertEqual(False, is_valid)


if __name__ == '__main__':
    unittest.main()
