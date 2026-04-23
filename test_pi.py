#!/usr/bin/env python3
"""
Tests for Pi Calculator
"""

import unittest
from pi_calculator import get_pi


class TestPiCalculator(unittest.TestCase):

    def test_pi_zero_decimals(self):
        self.assertEqual(get_pi(0), "3")

    def test_pi_five_decimals(self):
        result = get_pi(5)
        self.assertEqual(result, "3.14159")

    def test_pi_ten_decimals(self):
        result = get_pi(10)
        # Pi to 10 decimals: 3.1415926536
        self.assertEqual(result, "3.1415926536")

    def test_negative_decimals_raises_error(self):
        with self.assertRaises(ValueError):
            get_pi(-1)


if __name__ == "__main__":
    unittest.main()