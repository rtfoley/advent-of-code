import unittest
from day2 import Round, build_round, check_game, total_games, find_game_minimum

round_cases = [
    ("3 blue, 4 red", Round(4, 0, 3)),
    ("1 red, 2 green, 6 blue", Round(1, 2, 6)),
    ("2 green", Round(0, 2, 0)),
]


class TestSequence(unittest.TestCase):
    def test_build_round(self):
        for case, output in round_cases:
            with self.subTest():
                result = build_round(case)
                self.assertEqual(result.red, output.red)
                self.assertEqual(result.green, output.green)
                self.assertEqual(result.blue, output.blue)

    def test_round_valid(self):
        max_round = Round(4, 1, 5)
        round_valid_cases = [
            (Round(4, 0, 3), True),
            (Round(1, 2, 6), False),
            (Round(0, 2, 0), False),
        ]
        case: Round
        for case, output in round_valid_cases:
            with self.subTest():
                result = case.is_valid(max_round.red, max_round.green, max_round.blue)
                self.assertEqual(result, output)

    def test_check_game(self):
        cases = [
            ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 1),
            ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 2),
            (
                "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                0,
            ),
            (
                "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                0,
            ),
            ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 5),
        ]

        for case, output in cases:
            with self.subTest():
                result = check_game(case, 12, 13, 14)
                self.assertEqual(result, output)

    def test_total_games(self):
        games = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]

        result = total_games(games, 12, 13, 14)
        self.assertEqual(result, 8)

    def test_game_minimum(self):
        cases = [
            ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 48),
            ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 12),
            (
                "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                1560,
            ),
            (
                "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                630,
            ),
            ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 36),
        ]

        for case, output in cases:
            with self.subTest():
                result = find_game_minimum(case)
                self.assertEqual(result, output)


if __name__ == "__main__":
    unittest.main()
