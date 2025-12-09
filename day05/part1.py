"""
Advent of Code 2025 - Day 5 Part 1
"""

from util import read_input

def part1(data:str, verbose:bool=False) -> int:
    input = read_input(data)
    print("Ranges:")
    for i, line in enumerate(input):
        print(line)
        if line == "":
            break
    
    print("Ingredients:")
    for line in input[i+1:]:
        print(line)