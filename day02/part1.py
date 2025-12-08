"""
Advent of Code 2025 - Day 2 Part 1
"""

from util import read_input

def check_invalid(id):
    id = str(id)
    if len(id) % 2:
        return False
    if id[:len(id)//2] == id[len(id)//2:]:
        return True
    return False
    print(f"{id} -> {id[:len(id)//2]}|{id[len(id)//2:]}")

def part1(data):
    sum = 0
    p_input = read_input(data, "commas")
    for line in p_input:
        start, end = line.split("-")
        for id in range(int(start), int(end) + 1):
            if check_invalid(id):
                sum += id
    return sum