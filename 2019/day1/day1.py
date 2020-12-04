import sys
import math

def get_module_fuel(mass):
    fuel = math.floor(mass/3) - 2
    return fuel

def get_module_fuel_exp(mass):
    fuel = get_module_fuel(mass)
    if (fuel >= 0):
        return fuel + get_module_fuel_exp(fuel)
    else:
        return 0

def part1(raw_data):
    total_fuel = 0
    for module in raw_data:
        total_fuel += get_module_fuel(int(module))

    return total_fuel

def part2(raw_data):
    total_fuel = 0
    for module in raw_data:
        total_fuel += get_module_fuel_exp(int(module))

    return total_fuel

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        print("#1: ", part1(data))
        print("#2: ", part2(data))
