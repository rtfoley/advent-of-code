import re

def part1(raw_data):
    valid = 0 

    for line in raw_data:
        parsed = str(line).split(" ")
        bounds = [int(x) for x in parsed[0].split("-")]
        character = parsed[1][0]
        password = parsed[2]
        matches = password.count(character)
        if matches >= bounds[0] and matches <= bounds[1]:
            valid += 1

    return valid

def part2(raw_data):
    valid = 0 

    for line in raw_data:
        parsed = str(line).split(" ")
        positions = [int(x) for x in parsed[0].split("-")]
        character = parsed[1][0]
        password = parsed[2]
        if (password[positions[0]-1] == character) ^ (password[positions[1]-1] == character):
            valid += 1

    return valid


if __name__ == "__main__":
    with open("input.txt", "r") as raw:
        data = raw.readlines()
        print("#1: ", part1(data))
        print("#2: ", part2(data))
