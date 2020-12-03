import sys

def find_trees(raw_data, over, down):
    trees = 0

    for i in range(down, len(raw_data), down):
        if i >= len(raw_data):
            return trees

        column = int((i/down) * over % (len(raw_data[0]) -1))
        #print(f'row {i} column {column} {raw_data[i][column]}')
        if raw_data[i][column] == "#":
            trees += 1

    return trees

def part1(raw_data):
    return find_trees(raw_data, 3, 1)

def part2(raw_data):
    total_trees = 1
    slopes = [(1, 1),(3,1),(5,1),(7,1),(1,2)]
    for over, down in slopes:
        trees = find_trees(raw_data, over, down)
        print(f'{trees} for {over} over {down} down')
        total_trees *= trees

    return total_trees

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        print("#1: ", part1(data))
        print("#2: ", part2(data))
