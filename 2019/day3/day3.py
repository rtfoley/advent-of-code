import sys
import math

def get_points_for_segment(start, segment, steps):
    points = {(start): steps}
    for i in range(1, int(segment[1:]) + 1): 
        steps += 1
        point = (start[0], start[1])
        last_point =list(points)[-1]
        if segment[0] == 'R':
            point = (last_point[0] + 1, last_point[1])
        elif segment[0] == 'L':
            point = (last_point[0] - 1, last_point[1])
        if segment[0] == 'U':
            point = (last_point[0], last_point[1] + 1)
        elif segment[0] == 'D':
            point = (last_point[0], last_point[1] - 1)

        points[point] = steps

    return points

def get_points(wire):
    points = {}
    steps = 0
    startingPoint = (0, 0)
    for segment in wire:
        new_points = get_points_for_segment(startingPoint, segment, steps)
        points.update(new_points)
        startingPoint = list(points)[-1]
        steps = points[startingPoint]

    return points

def part1(wire1, wire2):
    wire1_points = get_points(wire1.split(","))
    wire2_points = get_points(wire2.split(","))

    intersections = list(set(wire1_points.keys()).intersection(wire2_points.keys()))
    intersections.remove((0,0))
    return min([abs(point[0]) + abs(point[1]) for point in intersections])

def part2(wire1, wire2):
    wire1_points = get_points(wire1.split(","))
    wire2_points = get_points(wire2.split(","))

    intersections = list(set(wire1_points.keys()).intersection(wire2_points.keys()))
    intersections.remove((0,0))
    return min(wire1_points[x] + wire2_points[x] for x in intersections)

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        print("#1: ", part1(data[0], data[1]))
        print("#2: ", part2(data[0], data[1]))
