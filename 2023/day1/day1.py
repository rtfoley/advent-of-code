import re


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}


def extract_value(line):
    trimmed = re.sub(r"\D", "", line)
    first = trimmed[0]
    last = trimmed[-1]
    return int(first+last)


def extract_number(input: str) -> int:
    return int(input) if input.isnumeric() else numbers[input]


def extract_value_with_text(line):
    # use lookahead ?= to handle overlaps like oneight (18)
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))"
    values = re.findall(pattern, line)
    first = extract_number(values[0])
    last = extract_number(values[-1])
    return (first*10)+last


def calculate_total(lines, use_text=False):
    total = 0
    for line in lines:
        line_value = extract_value_with_text(
            line) if use_text else extract_value(line)

        total += line_value

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        data = input.readlines()
        print(f"#1: {calculate_total(data)}")
        print(f"#2: {calculate_total(data, True)}")
