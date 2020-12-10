import sys
import re

def has_shiny_gold_child(overall_mapping, bag) -> bool:
    if bag is None:
        return False
    elif "shiny gold" in bag.keys():
        return True

    for inner_bag in bag.keys():
        if has_shiny_gold_child(overall_mapping, overall_mapping[inner_bag]):
            return True

    return False


def part1(data):
    rules = [re.findall("[\d]*[\s]?\w* \w* bag.*?", x) for x in data]
    
    # build a mapping of bag parent/child relationships
    mapping = {}
    for rule in rules:
        components = [x.replace("bag", "").strip() for x in rule]
        contents = {}
        pattern = re.compile(r'([\d])+[\s]?(\w* \w*)')
        for index in range(1, len(components)):
            if components[index] == "no other":
                contents = None

            result = pattern.match(components[index])
            if result is not None:
                contents[result.group(2)] = result.group(1)
            
        mapping[components[0]] = contents

    count = 0
    for bag in mapping:
        if has_shiny_gold_child(mapping, mapping.get(bag)):
            count += 1

    return count

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        print("#1: ", part1(data))
