import sys

def get_neighbors(data, rowNumber, columnNumber):
    neighbors = []
    rows = [x for x in range(len(data)) if rowNumber - 1 <= x <= rowNumber + 1]
    columns = [x for x in range(len(data[0])) if columnNumber - 1 <= x <= columnNumber + 1]
    for row in rows:
        for column in columns:
            if row != rowNumber or column != columnNumber:
                neighbors.append(data[row][column])

    return neighbors

def transform(data):
    occupied_seats = 0
    seats = [list(x) for x in data]
    length = len(seats[0])
    changed = False
    for row in range(len(seats)):
        for column in range(len(seats[0])):
            if(data[row][column] == "."):
                continue

            neighboring_seats = get_neighbors(data, row, column)
            occupied_count = sum([1 for x in neighboring_seats if x == "#"])

            if(data[row][column] == "L" and occupied_count == 0):
                seats[row][column] = "#"
            elif(data[row][column] == "#" and occupied_count >= 4):
                seats[row][column] = "L"

            if seats[row][column] != data[row][column]:
                changed = True

            if seats[row][column] == "#":
                occupied_seats += 1
    
    return seats, changed, occupied_seats

def part1(data):
    seats = [data, True]
    counter = 0
    while(seats[1]):
        seats = transform(seats[0])
        counter += 1

    return seats[2]

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        data = [x.replace("\n", "") for x in data]
        print("#1: ", part1(data))
