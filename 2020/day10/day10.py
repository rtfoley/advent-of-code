import sys

def part1(program):
    current = 0
    all_adapters = sorted(program)
    ending = all_adapters[-1] + 3
    differences = []
    
    for adapter in all_adapters:
        differences.append(adapter - current)
        current += (adapter - current)
            
    differences.append(ending - current)

    return sum([1 for x in differences if x == 1]) * sum([1 for x in differences if x == 3])

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        data = [int(x.replace("\n", "")) for x in data]
        print("#1: ", part1(data))
