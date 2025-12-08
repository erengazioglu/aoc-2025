"""
Advent of Code 2025 - Day 4 Part 1
"""

from util import read_input

def solve(map, w, h):
    print(map, w, h)

def part1(data:str, verbose:bool=False) -> int:
    map = []
    for line in read_input(data):
        map.append(line)
    solve(map, len(map[0]), len(map))