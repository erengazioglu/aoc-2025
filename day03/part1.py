"""
Advent of Code 2025 - Day 3 Part 1
"""

from util import read_input

def get_max_left(bank:str, verbose:bool=False) -> tuple[int, int]:
    max = (0, 0) # i, val
    for i, char in enumerate(bank[:-1]):
        if int(char) > max[1]:
            max = (i, int(char))
    if verbose:
        print(f"bank {bank} | max_left = {max}")
    return max


def get_max_right(bank:str, start:int, verbose:bool=False) -> tuple[int, int]:
    max = (0, 0) # i, val

    for i, char in enumerate(bank[start:]):
        if int(char) > max[1]:
            max = (i, int(char))
    if verbose:
        print(f"bank {bank} | max_right = {max}")
    return max


def get_largest_jolt(bank:str, verbose:bool=False):
    max_left = get_max_left(bank)
    max_right = get_max_right(bank, max_left[0] + 1)
    if verbose:
        print(f"bank {bank} | {max_left[1] * 10 + max_right[1]}")
    return max_left[1] * 10 + max_right[1]


def part1(data:str, verbose:bool=False):
    sum = 0
    for bank in read_input(data):
        sum += get_largest_jolt(bank, verbose)
    return sum