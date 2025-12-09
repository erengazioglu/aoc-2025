"""
Advent of Code 2025 - Day 5 Part 1
"""

from util import read_input

def parse(data:str, verbose:bool=False) -> tuple[list]:
    input = read_input(data)

    if verbose:
        print("Ranges:")
    ranges = []
    for i, line in enumerate(input):
        if verbose:
            print(line)
        if line == "":
            break
        ranges.append(tuple(int(limit) for limit in line.split("-")))
    
    if verbose:
        print("Ingredients:")
    ingredients = []
    for line in input[i+1:]:
        ingredients.append(int(line))
        if verbose:
            print(line)

    return (ranges, ingredients)

def is_fresh(id:str, ranges:list[tuple]) -> bool:
    for bounds in ranges:
        if id in range(bounds[0], bounds[1] + 1):
            return True
    return False


def part1(data:str, verbose:bool=False) -> int:
    ranges, ingredients = parse(data)
    if verbose:
        print("Ranges:\t\t", ranges)
        print("Ingredients:\t", ingredients)
    
    fresh = 0
    for id in ingredients:
        if is_fresh(id, ranges):
            if verbose:
                print(f"ID {id} is fresh!")
            fresh += 1
    return fresh