import sys
import re

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]

def part1(passports):
    valid = 0
    for passport in passports:
        if len([x for x in fields if x in passport]) == 7:
            valid += 1

    return valid

def part2(passports):
    valid = 0
    for passport in passports:
        fields = {key.split(":")[0]: key.split(":")[1] for key in passport.split(" ")}
        if not all([key in fields for key in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")]):
            continue

        try:
            byr = int(fields['byr'])
            iyr = int(fields['iyr'])
            eyr = int(fields['eyr'])
        except:
            #print (f'missing numeric field from {passport}')
            continue

        if byr < 1920 or byr > 2002:
            #print (f'invalid BYR {byr} in {passport}')
            continue
        elif iyr < 2010 or iyr > 2020:
            #print (f'invalid IYR {iyr} in {passport}')
            continue
        elif eyr < 2020 or eyr > 2030:
            #print (f'invalid EYR {eyr} in {passport}')
            continue

        hcl_regex = re.compile(r'^#[0-9a-f]{6}$')
        if hcl_regex.search(fields['hcl']) is None:
            #print (f'invalid HCL {fields["hcl"]} in {passport}')
            continue
    
        pid_regex = re.compile(r'^[0-9]{9}$')
        if pid_regex.search(fields['pid']) is None:
            #print (f'invalid PID {fields["pid"]} in {passport}')
            continue

        if fields['ecl'] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            #print (f'invalid ECL {fields["ecl"]} in {passport}')
            continue

        height = int(fields['hgt'][:-2])
        height_units = fields['hgt'][-2:]

        if height_units is None or height_units not in ("in", "cm"):
            continue
        if height_units=="in" and (height < 59 or height > 76):
            #print (f'invalid HGT {fields["hgt"]} in {passport}')
            continue
        elif height_units=="cm" and (height < 150 or height > 193):
            #print (f'invalid HGT {fields["hgt"]} in {passport}')
            continue

        #print([byr, iyr, eyr, "{:03d}".format(height), height_units, fields['hcl'], fields['ecl'], fields['pid']])

        valid += 1

    return valid
            

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.read()
        passports = [x.replace("\n", " ") for x in data.split("\n\n")]
        print("#1: ", part1(passports))
        print(f'#2 {part2(passports)} of {len(passports)}')
