import string

checks = [
    # x, y
    [0, -1],
    [1, -1],
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
]


def get_part_numbers(lines):
    numbers = []
    row_count = len(lines)
    col_count = len(lines[0])
    line: str
    for row, line in enumerate(lines):
        number = 0
        is_marked = False
        for column, value in enumerate(line):
            if not value in string.digits:
                if number > 0:
                    if is_marked:
                        numbers.append(number)
                        is_marked = False

                    number = 0

                continue

            number = int(value) if number == 0 else (number * 10) + int(value)

            # finished a number at the end of the row, save if marked
            if column == col_count - 1:
                if is_marked:
                    numbers.append(number)
                    is_marked = False

                number = 0

            if is_marked:
                continue

            for check in checks:
                # verify check address is in bounds
                check_row = row + check[0]
                check_col = column + check[1]
                if (
                    check_row < 0
                    or check_row >= row_count
                    or check_col < 0
                    or check_col >= col_count
                ):
                    continue

                check_value = lines[check_row][check_col]
                is_marked = check_value in string.punctuation and not check_value == "."

                if is_marked:
                    break

    return numbers


def get_part_number_sum(lines):
    numbers = get_part_numbers(lines)
    total = 0
    for number in numbers:
        total += number

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        data = input.readlines()

        print(f"#1: {get_part_number_sum(data)}")
        print(f"#2: {2}")
