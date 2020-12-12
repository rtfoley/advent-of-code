import sys
from collections import defaultdict

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

def part2(data):
    # 1456710
    # 1 has 1 path
    # 4 has 1 path
    # 5 has 1 path
    # 6 has 2 paths
    # 7 has 4 paths, 4-7, 4-5-7, 4-6-7, 4-5-6-7, sum of paths from previous 3 numbers
    # 10 has 1 path
    all_adapters = sorted(data)
    paths = defaultdict(int)
    paths[0] = 1
    for adapter in all_adapters:
        paths[adapter] = 0
        paths[adapter] = paths[adapter-1] + paths[adapter-2] + paths[adapter-3]

    return max([x for key, x in paths.items()])


if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        data = [int(x.replace("\n", "")) for x in data]
        print("#1: ", part1(data))
        print("#2: ", part2(data))
