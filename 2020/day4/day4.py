import sys

def part1(passports):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional_fields = ["cid"]

    valid = 0
    for passport in passports:
        if len([x for x in fields if x in passport]) == 7:
            valid += 1

    return valid
            

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.read()
        passports = [x.replace("\n", " ") for x in data.split("\n\n")]
        print("#1: ", part1(passports))
        #print("#2: ", part2(data[0], data[1]))
