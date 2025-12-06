"""
Advent of Code 2025 - Day 1
"""

from util import read_input

def count_clicks(dial, turns):
    clicks = abs(turns) // 100
    if turns < 0:
        turns = turns % 100 - 100
    else:
        turns %= 100
    if (dial + turns >= 100) \
    or (dial > 0 and dial + turns <= 0) \
    or (dial < 0 and dial + turns >= 0) \
    or (dial + turns <= -100):
        clicks += 1
    return clicks

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

def part2(data="inputs/01-sample"):
    dial = 50
    password = 0

    for line in read_input(data):
        turns = int(line[1:])
        if line[0] == 'L':
            turns *= -1
        password += count_clicks(dial, turns)
        dial = (dial + turns) % 100
    
    return password
    # return "(TBD)"

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