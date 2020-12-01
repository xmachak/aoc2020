from itertools import combinations


def read_input():
    with open('input/day1.txt', 'r') as reader:
        entries = [int(entry) for entry in reader.read().splitlines()]
    return entries


def find_two(entries):
    for entry in entries:
        if 2020-entry in entries:
            return entry*(2020-entry)


def find_three(entries):
    for group in combinations(entries, 3):
        if sum(group) == 2020:
            return group[0]*group[1]*group[2]


if __name__ == '__main__':
    report = read_input()
    print(find_two(report))
    print(find_three(report))

