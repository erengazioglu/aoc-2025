"""
Advent of Code 2025 - Day 7 Part 2
"""

from util import read_input, add

def display_line(line, beams):
    display = ""
    for pos, count in enumerate(beams):
        if count > 0:
            display += "|"
        else:
            display += line[pos]
    print(display)


def process_line(line, beams, verbose=False):
    for pos, count in enumerate(beams):
        if line[pos] == "^":
            beams[pos] -= count
            beams[pos + 1] += count
            beams[pos - 1] += count
    if verbose:
        display_line(line, beams)


def part2(data:str, verbose:bool=False) -> int:
    input = read_input(data)
    beams = [0] * len(input[0])
    beams[input[0].find("S")] = 1
    # print(beams)
    for line in input:
        process_line(line, beams, verbose)

    return add(*beams)