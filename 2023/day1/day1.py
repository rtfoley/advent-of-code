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


# this is not an elegant solution, but it works
doubles = {
    "twone": 21,
    "threeight": 38,
    "fiveight": 58,
    "eightwo": 82,
    "eighthree": 83
}


def extract_value(line):
    trimmed = re.sub(r"\D", "", line)
    first = trimmed[0]
    last = trimmed[-1]
    return int(first+last)


def extract_number(input: str) -> int:
    return int(input) if input.isnumeric() else numbers[input]


def extract_value_with_text(line):
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))"
    for double in doubles:
        line = re.sub(double, str(doubles[double]), line)
    values = re.findall(pattern, line)
    print(values)
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
