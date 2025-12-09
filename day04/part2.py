"""
Advent of Code 2025 - Day 4 Part 2
"""

from util import read_input
from .part1 import is_paper, is_accessible

def replace_index(s:str, i:int, c:str) -> str:
    return s[:i] + c + s[i+1:]


def remove_paper(map, cell) -> list[str]:
    map[cell[1]] = replace_index(map[cell[1]], cell[0], ".")
    return map


def part2(data:str, verbose:bool=False) -> int:
    map = read_input(data)
    w = len(map[0])
    h = len(map)

    total = 0
    while True:
        replace = 0
        if verbose:
            for line in map:
                print(line)
        for y, row in enumerate(map):
            for x, cell in enumerate(row):
                if is_accessible(map, w, h, (x, y)):
                    remove_paper(map, (x, y))
                    replace += 1
        if replace == 0:
            break
        total += replace
        if verbose:
            print("-" * w)
    return total
    