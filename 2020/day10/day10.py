import sys

def part1(program):
    current = 0
    ending = max(program) + 3
    differences = []
    while current != ending:
        adapters = [x for x in program if current < x <= current + 3]
        if len(adapters) == 0:
            return None
        
        adapter = min(adapters)
        differences.append(adapter - current)
        current += (adapter - current)
        if ending - current <= 3:
            differences.append(ending - current)
            current = ending

    return sum([1 for x in differences if x == 1]) * sum([1 for x in differences if x == 3])

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        data = [int(x.replace("\n", "")) for x in data]
        print("#1: ", part1(data))
