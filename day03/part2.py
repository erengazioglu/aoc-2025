"""
Advent of Code 2025 - Day 3 Part 2
"""

from util import read_input

def get_max(bank:str, verbose:bool=False) -> tuple[int, int]:
    max = (0, 0) # i, val

    for i, char in enumerate(bank):
        if int(char) > max[1]:
            max = (i, int(char))
    if verbose:
        print(f"bank {bank} | max = {max}")
    return max

def part2(data:str, verbose:bool=False) -> int:
    return read_input(data)