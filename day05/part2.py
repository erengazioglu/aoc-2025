"""
Advent of Code 2025 - Day 5 Part 2
"""

from .part1 import parse

def part2(data:str, verbose:bool=False) -> int:
    ranges, _ = parse(data)
    if verbose:
        print("Ranges:\t\t", ranges)
    
    fresh = set()
    for start, end in ranges:
        fresh.update(range(start, end + 1))

    print(fresh, len(fresh), sep=": ")
    return len(fresh)