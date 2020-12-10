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

def build_mapping(data):
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

    return mapping

def part1(mapping):
    count = 0
    for bag in mapping:
        if has_shiny_gold_child(mapping, mapping.get(bag)):
            count += 1

    return count

def get_child_count(overall_mapping, bag) -> int:
    full_bag = overall_mapping.get(bag)
    if full_bag is None:
        return 0
    
    count = 0
    for inner_bag, bag_count in full_bag.items():
        child_count = get_child_count(mapping, inner_bag)
        count += int(bag_count) + int(bag_count) * child_count

    return count

def part2(mapping):
    return get_child_count(mapping, "shiny gold")
    

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.readlines()
        mapping = build_mapping(data)
        print("#1: ", part1(mapping))
        print("#2: ", part2(mapping))
