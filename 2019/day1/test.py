import unittest
from day1 import get_module_fuel, get_module_fuel_exp

cases = [(12,2),(14,2),(1969,654),(100756,33583)]
exp_cases = [(14,2),(1969,966),(100756,50346)]

class TestSequence(unittest.TestCase):
    def test_fuel(self):
        for mass, expected_fuel in cases:
            with self.subTest():
                result = get_module_fuel(mass)
                self.assertEqual(result, expected_fuel)

    def test_fuel_exp(self):
        for mass, expected_fuel in exp_cases:
            with self.subTest():
                result = get_module_fuel_exp(mass)
                self.assertEqual(result, expected_fuel)

if __name__ == '__main__':
    unittest.main()