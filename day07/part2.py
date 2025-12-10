"""
Advent of Code 2025 - Day 7 Part 2
"""

from util import read_input

def process_line(line, beams):
    chars = line
    # print(f"beams: {beams}")
    new_beams = []
    for b in beams:
        # if chars[b] == ".":
            # chars[b] = "|"
            # new_beams.append(b)
        if chars[b] in ".|S":
            new_beams.append(b)
        else:
            new_beams.append(b - 1)
            new_beams.append(b + 1)
            # if chars[b - 1] == ".":
            #     chars[b - 1] = "|"
            # if chars[b + 1] == ".":
            #     chars[b + 1] = "|"
                # print(f"new beam: {i}")
    # print(f"new beams: {new_beams}")
    return("".join(chars), new_beams)


def part2(data:str, verbose:bool=False) -> int:
    input = read_input(data)
    beams = []
    beams.append(input[0].find("S"))
    for n, line in enumerate(input):
        input[n], beams = process_line(line, beams)
        print(f"line {n:03} : {input[n]}, timelines = {len(beams)}")
        # print(f"beams: {beams}")
        # print(input[n])
    return len(beams)