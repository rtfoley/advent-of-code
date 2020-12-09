import unittest
from day5 import getSubset, getSeat

cases = [
    ("F", [0, 127], [0,63]),
    ("B", [0, 127], [64,127]),
    ("L", [0, 7], [0,3]),
    ("R", [0, 7], [4,7]),
    ("F", [44, 45], [44, 44])
]

boarding_passes = [
    ("FBFBBFFRLR", 357),
    ("BFFFBBFRRR", 567),
    ("FFFBBBFRRR", 119),
    ("BBFFBBFRLL", 820),
    ("FFFFBFBLRR", 43),
    ("FFFFBFBRRR", 47)
]

class TestSequence(unittest.TestCase):
    def test_bounds(self):
        for character, bounds, expected in cases:
            with self.subTest():
                result = getSubset(character, bounds)
                self.assertEqual(result, expected)

    def test_passes(self):
        for boarding_pass, expected in boarding_passes:
            with self.subTest():
                result = getSeat(boarding_pass)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()