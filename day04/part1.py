"""
Advent of Code 2025 - Day 4 Part 1
"""

from util import read_input

def is_paper(map, w, h, cell, verbose:bool=False) -> bool:
    if cell[0] < 0 \
    or cell[0] > w - 1 \
    or cell[1] < 0 \
    or cell[1] > h - 1:
        if verbose:
            print(f"Cell {cell} out of bounds, therefore it can't be paper.")
        return False
    return map[cell[1]][cell[0]] == '@'


def is_accessible(map:list[str], w:int, h:int, cell:tuple[int, int], verbose:bool=False) -> bool:
    if verbose:
        print(f"cell{cell}({map[cell[1]][cell[0]]}) -> {"paper" if is_paper(map, w, h, cell) else "not paper"}")
    if not is_paper(map, w, h, cell):
        return False
    papers = 0
    # check top and bottom
    for x in range(cell[0] - 1, cell[0] + 2):
        for y in (cell[1] - 1, cell[1] + 1):
            papers += int(is_paper(map, w, h, (x, y), verbose))
            if papers >= 4:
                return False
    # check sides
    for x in (cell[0] - 1, cell[0] + 1):
        papers += int(is_paper(map, w, h, (x, cell[1]), verbose))
        if papers >= 4:
            return False
    return True


    # for x in range(cell[0] - 1, cell[0] + 2):
    #     papers += int(is)
    #     for y in range(cell[1] - 1, cell[1] + 2):
    #         papers += int(is_paper(map, w, h, (x, y), verbose))
    #         if papers >= 4:
    #             return False
    return True


def part1(data:str, verbose:bool=False) -> int:
    map = read_input(data)
    w = len(map[0])
    h = len(map)
    if verbose:
        for line in map:
            print(line)

    total = 0
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if verbose and is_accessible(map, w, h, (x, y)):
                print(f"({x},{y}) is accessible!")
            total += int(is_accessible(map, w, h, (x, y)))
    return total