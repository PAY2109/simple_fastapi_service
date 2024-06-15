import unittest

from deposit_service import calculate_deposit


class TestCalculateDeposit(unittest.TestCase):
    def test_calculate_deposit(self):
        payload = {'date': '31.01.2021', 'periods': 3, 'amount': 10000, 'rate': 6.0}
        calculated_deposit_details = calculate_deposit(payload)
        expected_deposit_details = {
            "31.01.2021": 10050.0,
            "28.02.2021": 10100.25,
            "31.03.2021": 10150.75
        }
        self.assertEqual(expected_deposit_details, calculated_deposit_details)


if __name__ == '__main__':
    unittest.main()
