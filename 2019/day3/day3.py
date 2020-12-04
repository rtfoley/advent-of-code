import sys
import math

def get_points_for_segment(start, segment):
    points = [(start)]
    for i in range(1, int(segment[1:]) + 1):        
        if segment[0] == 'R':
            points.append((points[-1][0] + 1, points[-1][1]))
        elif segment[0] == 'L':
            points.append((points[-1][0] - 1, points[-1][1]))
        if segment[0] == 'U':
            points.append((points[-1][0], points[-1][1] + 1))
        elif segment[0] == 'D':
            points.append((points[-1][0], points[-1][1] - 1))

    return points

def get_points(wire):
    points = []
    startingPoint = (0, 0)
    for segment in wire:
        new_points = get_points_for_segment(startingPoint, segment)
        points.extend(new_points)
        startingPoint = points[-1]

    return points

def part1(wire1, wire2):
    wire1_points = get_points(wire1.split(","))
    wire2_points = get_points(wire2.split(","))

    intersections = list(set(wire1_points).intersection(wire2_points))
    intersections.remove((0,0))
    return min([abs(point[0]) + abs(point[1]) for point in intersections])
    

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        print("#1: ", part1(data[0], data[1]))
