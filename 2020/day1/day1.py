def part1(numbers):
    for number in numbers:
        for other in numbers:
            if(number + other == 2020):
                return number * other

def part2(numbers):
    for number in numbers:
        for second in numbers:
            for third in numbers:
                if(number + second + third == 2020):
                    return number * second * third

if __name__ == "__main__":
    with open("input.txt", "r") as raw:
        data = raw.readlines()
        input = [int(x) for x in data]

        print("#1: ", part1(input))
        print("#2: ", part2(input))
