import unittest
from day1 import part1, part2

data = [1721, 979, 366, 299, 675, 1456]

class TestDay1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1(data), 514579)

    def test_part2(self):
        self.assertEqual(part2(data), 241861950)

if __name__ == '__main__':
    unittest.main()