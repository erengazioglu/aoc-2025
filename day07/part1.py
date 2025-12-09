"""
Advent of Code 2025 - Day 7 Part 1
"""

from util import read_input, replace_index

def process_line(line, beams, splits):
    for i, char in enumerate(line):
        if i in beams:
            if char == ".":
                line = replace_index(line, i, "|")
            elif char == "^":
                beams.discard(i)
                for j in (i-1, i+1):
                    beams.add(j)
                    if line[j] == ".":
                        line = replace_index(line, j, "|")
                splits += 1
    return (line, beams, splits)

def part1(data:str, verbose:bool=False) -> int:
    input = read_input(data)
    beams = set()
    beams.add(input[0].find("S"))
    splits = 0
    for n, line in enumerate(input):
        print(f"line {n:03} : {line}")
        input[n], beams, splits = process_line(line, beams, splits)
        # print(input[n])
    print("\nFINISHED RESULT\n---")
    for n, line in enumerate(input):
        print(f"line {n:03} : {line}")
    return splits
    # return read_input(data)