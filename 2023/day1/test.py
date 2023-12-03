import unittest
from day1 import extract_value, calculate_total, extract_value_with_text, extract_number

cases = [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77)
]

text_cases = [
    ("two1nine", 29),
    ("eightwothree", 83),
    ("abcone2threexyz", 13),
    ("xtwone3four", 24),
    ("4nineeightseven2", 42),
    ("zoneight234", 14),
    ("7pqrstsixteen", 76),
    ("pkdrhksqdhrvhg5", 55),
    ("ninebfour26fivetwonem", 91),
    ("oneight", 18)
]


number_cases = [
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 7),
    ("8", 8),
    ("9", 9),
    ("0", 0),
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
    ("zero", 0),
]


class TestSequence(unittest.TestCase):
    def test_extract_value(self):
        for case, output in cases:
            with self.subTest():
                result = extract_value(case)
                self.assertEqual(result, output)

    def test_total(self):
        lines = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet"
        ]

        result = calculate_total(lines)
        self.assertEqual(result, 142)

    def test_extract_value_with_text(self):
        for case, output in text_cases:
            with self.subTest():
                result = extract_value_with_text(case)
                self.assertEqual(result, output)

    def test_total_with_text(self):
        lines = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen"
        ]

        result = calculate_total(lines, True)
        self.assertEqual(result, 281)

    def test_extract_number(self):
        for case, output in number_cases:
            with self.subTest():
                result = extract_number(case)
                self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
