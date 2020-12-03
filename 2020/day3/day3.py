def part1(raw_data):
    trees = 0
    length = len(raw_data[0])

    for i in range(1, len(raw_data), 1):
        if i >= len(raw_data):
            return trees

        column = i * 3 % (length -1)
        if raw_data[i][column] == "#":
            trees += 1

    return trees


if __name__ == "__main__":
    with open("input.txt", "r") as raw:
        data = raw.readlines()
        print("#1: ", part1(data))
