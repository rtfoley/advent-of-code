def find_pair_of_sum(sum, numbers):
    complements = { (sum - number):number for number in numbers}
    return next(((number, complements[number]) for number in numbers if number in complements.keys()), None)

def part1(numbers):
    values = find_pair_of_sum(2020, numbers)
    return values[0]*values[1]

def part2(numbers):
    triples = { number:(find_pair_of_sum(2020-number, numbers)) for number in numbers}
    value = next(((number, triples[number][0], triples[number][1]) for number in numbers if number in triples.keys() and triples[number] is not None), None)
    return value[0]*value[1]*value[2]

if __name__ == "__main__":
    with open("input.txt", "r") as raw:
        data = raw.readlines()
        input = [int(x) for x in data]

        print("#1: ", part1(input))
        print("#2: ", part2(input))