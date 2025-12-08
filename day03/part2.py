"""
Advent of Code 2025 - Day 3 Part 2
"""

from util import read_input

def get_max(bank:str, start:int=0, verbose:bool=False) -> tuple[int, int]:
    max = (0, 0) # i, val

    for i, char in enumerate(bank[start:]):
        if int(char) > max[1]:
            max = (start + i, int(char))
    if verbose:
        print(f"bank {bank} search {bank[start:]} | max = {max}")
    return max

def get_joltage(bank:str, verbose:bool=False) -> int:
    size = 12
    i = 0
    joltage = ""

    while size > 0:
        if (size > 1):
            max = get_max(bank[:(size - 1) * -1], i, verbose)
        else:
            max = get_max(bank, i, verbose)
        joltage += str(max[1])
        size -= 1
        i = max[0] + 1

    if verbose:
        print(f"bank {bank} | joltage {joltage}")
    return int(joltage)

def part2(data:str, verbose:bool=False) -> int:
    sum = 0
    for bank in read_input(data):
        sum += get_joltage(bank, verbose)
    return sum