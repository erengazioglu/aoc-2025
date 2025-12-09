"""
Advent of Code 2025 - Day 6 Part 2
"""

from util import read_input
from .part1 import add, multiply

def parse_column(input, col, rows, verbose=False):
    number = 0
    skips = 0
    for i, row in enumerate(reversed(range(rows - 1))):
        if input[row][col] == " ":
            skips += 1
        else:
            number += int(input[row][col]) * pow(10, i - skips)
            if verbose:
                print(f"row {row} col {col}: {int(input[row][col])} multiplied by {pow(10, i)} -> number {number}")
    operation = input[rows - 1][col]

    return (number, operation)

def part2(data:str, verbose:bool=False) -> int:
    input = read_input(data)
    if verbose:
        for line in input:
            print(line)

    rows = len(input)
    cols = len(input[0])
    cache = []
    acc = 0
    for col in reversed(range(cols)):
        number, operation = parse_column(input, col, rows)
        if number != 0:
            cache.append(number)
        if operation in "*+":
            if operation == "*":
                acc += multiply(*cache)
            else:
                acc += add(*cache)
            if verbose:
                print(f"op {operation}", *cache, f"-> ({acc})")
            cache.clear()
    return acc
    # return read_input(data)