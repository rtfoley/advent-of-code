import sys

def part1(groups):
    adj_groups = [x.replace("\n", "") for x in groups]
    count = 0
    for group in adj_groups:
        count += len(set(group))

    return count

def part2(groups):
    count = 0
    adj_groups = [x.split("\n") for x in groups]
    for group in adj_groups:
        question_count = 0
        questions = {}
        for person in group:
            for question in person:
                if question in questions.keys():
                    questions[question] += 1
                else:
                    questions[question] = 1
        
        all_qs = [key for key,value in questions.items() if value == len(group)]
        count += len(all_qs)

    return count

if __name__ == "__main__":
    with open(sys.argv[1], "r") as raw:
        data = raw.read()
        groups = data.split("\n\n")
        print("#1: ", part1(groups))
        print("#2: ", part2(groups))
