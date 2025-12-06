"""
Advent of Code 2025 - Day 1
"""

from util import read_input


def part1(data="inputs/01-full"):
    dial = 50
    password = 0

    for line in read_input(data):
        sign = 1
        if line[0] == 'L':
            sign = -1
        dial += int(line[1:]) * sign
        dial %= 100
        if (dial == 0):
            password += 1
        
    return password


def part2(data="inputs/01-full"):
    """Solve part 2 of the puzzle."""
    # TODO: Implement part 2 solution
    return read_input(data)


if __name__ == '__main__':
    data = read_input("../inputs/01-sample")
    
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))



"""
    for line in read_input(data):
        sign = 1
        if line[0] == 'L':
            sign = -1
        password += int(line[1:]) * sign
        password %= 100
"""