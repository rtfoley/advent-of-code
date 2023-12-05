import unittest
from day3 import get_part_numbers


class TestSequence(unittest.TestCase):
    def test_something(self):
        data = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
            ".123.456..",
            "..........",
            ".789.987..",
            "..........",
            ".333*444..",
        ]

        result = get_part_numbers(data)
        expected = [467, 35, 633, 617, 592, 755, 664, 598, 333, 444]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
