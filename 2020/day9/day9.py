import sys

def is_valid(number, buffer):
    for buffer_number in buffer:
        if number - buffer_number in buffer:
            return True

    return False

def part1(program, size):
    buffer = program[:4]

    for index in range(size, len(program)):
        number = program[index]
        if is_valid(number, program[index-size:index]):
            continue

        return number

def part2(program):
    target = 15690279
    for index in range(len(program)):
        sum = 0
        for test_index in range(index, len(program)):
            number = program[test_index]
            sum += program[test_index]
            if sum == target:
                return min(program[index:test_index]) + max(program[index:test_index])
            elif sum >= target:
                continue

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        data = [int(x.replace("\n", "")) for x in data]
        print("#1: ", part1(data, 25))
        print("#2: ", part2(data))
