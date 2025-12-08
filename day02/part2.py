"""
Advent of Code 2025 - Day 2 Part 2
"""

from util import read_input

def check_substr(id:str, id_len:int, sub_len:int, verbose:bool=False) -> bool:
    # e.g. 1323 1323 1323, 4 will return True
    if id_len % sub_len:
        if verbose:
            print(f"{id} | skipping sub_len={sub_len}")
        return False
    
    i = 0
    while i < sub_len:
        sub_i = 0
        while sub_i * sub_len < id_len:
            if verbose:
                print(f"{id} | id[{i}] != id[{i} + {sub_i} * {sub_len}]]")
            if id[i] != id[i + sub_i * sub_len]:
                return False
            sub_i += 1
        i += 1
    
    return True


def check_invalid(id:int, verbose:bool=False) -> bool:
    id = str(id)
    id_len = len(id)
    sub_len = 1

    while sub_len <= id_len // 2:
        if check_substr(id, id_len, sub_len, verbose):
            return True
        sub_len += 1

    return False


def part2(data:str, verbose:bool=False) -> int:
    sum = 0
    p_input = read_input(data, "commas")
    for line in p_input:
        start, end = line.split("-")
        for id in range(int(start), int(end) + 1):
            if check_invalid(id, verbose):
                sum += id
    return sum