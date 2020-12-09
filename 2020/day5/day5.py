import sys
import re

def getSubset(character, bounds):
    length = int((bounds[1] - bounds[0] + 1)/2)
    if character in ['F', 'L']:
        return [bounds[0], bounds[0] + length - 1]
    else:
        return [bounds[1] - length + 1, bounds[1]]

def getSeat(boarding_pass):
    this_pass = boarding_pass.replace("\n", "", 1)
    rows = this_pass[0:7]
    seats = this_pass[-3:]

    row = [0, 127]
    for row_direction in rows:
        row = getSubset(row_direction, row)

    seat = [0,7]
    for seat_direction in seats:
        seat = getSubset(seat_direction, seat)

    id = (row[0] * 8) + seat[0]
    return id

def part1(passes):
    seats = [getSeat(x) for x in passes]
    return max(seats)

def part2(passes):
    seats = [getSeat(x) for x in passes]
    for x in range(len(seats) + 1):
        if x not in seats and x+1 in seats and x-1 in seats:
            return x

    return -1

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        print("#1: ", part1(data))
        print('#2: ', part2(data))
