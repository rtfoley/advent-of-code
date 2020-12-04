import sys
import math

def run_opcode(program):
    for i in range(0, len(program), 4):
        opcode = program[i]
        #print(f'opcode {opcode} at position {i}')

        if opcode == 99:
            return program

        # first address
        p1 = program[i+1]

        # second address
        p2 = program[i+2]

        # result address
        p3 = program[i+3]

        if opcode == 1:
            program[p3] = program[p1] + program[p2]
        elif opcode == 2:
            program[p3] = program[p1] * program[p2]

    return program

def part1(program):
    program[1] = 12
    program[2] = 2
    result = run_opcode(program)
    return result[0]

def part2(program):
    for noun in range(0, 99):
        for verb in range(0, 99):
            # copy the program ensure fresh data for each test
            test_program = program[:]
            test_program[1] = noun
            test_program[2] = verb
            result = run_opcode(test_program)
            if result[0] == 19690720:
                return 100 * noun + verb
    
    return 0

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.read()
        program = [int(x) for x in data.split(",")]
        #print("#1: ", part1(program))
        print("#2: ", part2(program))
