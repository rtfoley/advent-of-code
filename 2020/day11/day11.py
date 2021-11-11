import sys

directions = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
]


def get_neighbors(data, rowNumber, columnNumber):
    neighbors = []
    for (row, col) in directions:
        newRow = rowNumber + row
        newColumn = columnNumber + col
        if newRow in range(len(data)) and newColumn in range(len(data[0])):
            neighbors.append(data[newRow][newColumn])

    return neighbors


def get_seat_neighbors(data, rowNumber, columnNumber):
    neighbors = []
    for (row, col) in directions:
        newRow = rowNumber + row
        newColumn = columnNumber + col
        while newRow in range(len(data)) and newColumn in range(len(data[0])):
            if data[newRow][newColumn] != '.':
                neighbors.append(data[newRow][newColumn])
                break

            newRow += row
            newColumn += col

    return neighbors


def transform(data, threshold, neighbor_finder):
    occupied_seats = 0
    seats = [list(x) for x in data]
    length = len(seats[0])
    changed = False
    for row in range(len(seats)):
        for column in range(len(seats[0])):
            if(data[row][column] == "."):
                continue

            neighboring_seats = neighbor_finder(data, row, column)
            occupied_count = sum([1 for x in neighboring_seats if x == "#"])

            if(data[row][column] == "L" and occupied_count == 0):
                seats[row][column] = "#"
            elif(data[row][column] == "#" and occupied_count >= threshold):
                seats[row][column] = "L"

            if seats[row][column] != data[row][column]:
                changed = True

            if seats[row][column] == "#":
                occupied_seats += 1

    return seats, changed, occupied_seats


def run(data, threshold, neighbor_finder):
    seats = [data, True]
    counter = 0
    while(seats[1]):
        seats = transform(seats[0], threshold, neighbor_finder)
        counter += 1

    return seats[2]


if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        data = [x.replace("\n", "") for x in data]
        print("#1: ", run(data, 4, get_neighbors))
        print("#2: ", run(data, 5, get_seat_neighbors))
