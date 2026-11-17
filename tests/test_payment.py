import unittest

from src.payment.payment import calculate_total


class PaymentTests(unittest.TestCase):
    def test_without_fee(self):
        self.assertEqual(calculate_total(100), 100)

    def test_with_fee(self):
        self.assertEqual(calculate_total(100, 2.5), 102.5)


if __name__ == "__main__":
    unittest.main()
