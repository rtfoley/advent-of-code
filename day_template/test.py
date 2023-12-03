import unittest


class TestSequence(unittest.TestCase):
    def test_something(self):
        cases = [
            (1, 1),
            (1, 2),
            (1, 3),
        ]
        for case, output in cases:
            with self.subTest():
                result = case
                self.assertEqual(result, output)


if __name__ == "__main__":
    unittest.main()
