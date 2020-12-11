import sys

def run_program(program, should_error):
    accumulator = 0
    pointer = 0
    instructions_run = []
    while(pointer not in instructions_run and pointer < len(program)):
        instruction = program[pointer]
        instructions_run.append(pointer)
        segments = instruction.split(" ")

        is_plus = segments[1][0] == "+"
        value = int(segments[1][1:])
        if segments[0] == "nop":
            pointer += 1
        elif segments[0] == "acc":
            if is_plus:
                accumulator += value
            else:
                accumulator -= value

            pointer += 1
        elif segments[0] == "jmp":
            if is_plus:
                pointer += value
            else:
                pointer -= value

    terminated = pointer == len(program)
    return terminated, accumulator

def part2(program):
    for index in range(len(program)):
        copy = [x for x in program]
        instruction = str(copy[index])
        if "nop" in instruction:
            copy[index] = instruction.replace("nop", "jmp")
        elif "jmp" in instruction:
            copy[index] = instruction.replace("jmp", "nop")
        else:
            continue

        value = run_program(copy, True)
        if value[0] == True:
            return value[1]
        
    return -1

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        print("#1: ", run_program(data, False)[1])
        print("#2: ", part2(data))
