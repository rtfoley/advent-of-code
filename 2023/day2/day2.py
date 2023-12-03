class Round:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def is_valid(self, red_limit, green_limit, blue_limit):
        return (
            self.red <= red_limit
            and self.green <= green_limit
            and self.blue <= blue_limit
        )


def build_round(line: str) -> Round:
    counts = line.split(",")
    red = 0
    green = 0
    blue = 0
    for count in counts:
        count = count.lstrip().rstrip()
        split = count.split(" ")
        value = int(split[0])
        if split[1] == "red":
            red = value
        elif split[1] == "green":
            green = value
        else:
            blue = value

    return Round(red, green, blue)


def check_game(line: str, max_red, max_green, max_blue):
    sections = line.split(":")
    id = int(sections[0].split(" ")[1])
    rounds = sections[1].split(";")

    for raw_round in rounds:
        round = build_round(raw_round)
        if not round.is_valid(max_red, max_green, max_blue):
            return 0

    return id


def total_games(lines, max_red, max_green, max_blue):
    total = 0
    for line in lines:
        total += check_game(line, max_red, max_green, max_blue)

    return total


def find_game_minimum(line: str):
    sections = line.split(":")
    rounds = sections[1].split(";")

    min_red = 0
    min_green = 0
    min_blue = 0
    for raw_round in rounds:
        round = build_round(raw_round)
        if round.red > min_red:
            min_red = round.red

        if round.green > min_green:
            min_green = round.green

        if round.blue > min_blue:
            min_blue = round.blue

    return min_red * min_green * min_blue


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        data = input.readlines()
        valid_total = 0
        power_total = 0
        for line in data:
            valid_total += check_game(line, 12, 13, 14)
            power_total += find_game_minimum(line)
        print(f"#1: {valid_total}")
        print(f"#2: {power_total}")
