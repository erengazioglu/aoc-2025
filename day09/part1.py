"""
Advent of Code 2025 - Day 9 Part 1
"""

from util import read_input

def rect(p1, p2) -> int:
    return ((abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1))

def part1(data:str, verbose:bool=False) -> int:
    input = read_input(data, type="tuples")
    max = 0
    for i, point in enumerate(input):
        i += 1
        while i < len(input):
            # print(f"rect {point} {input[i]} = {rect(point, input[i])}")
            new_rect = rect(point, input[i])
            if new_rect > max:
                max = new_rect
            i += 1
    return max
    # return read_input(data, type="tuples")