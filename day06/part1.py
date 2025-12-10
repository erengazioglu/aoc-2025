"""
Advent of Code 2025 - Day 6 Part 1
"""

from util import read_input, add, multiply


def remove_all(arr:list, elem) -> list:
    new_arr = []
    for item in arr:
        if item != elem:
            new_arr.append(item)
    return new_arr

def parse(data:str) -> list[tuple]:
    result = list(zip(*[remove_all(line.split(" "), "") for line in read_input(data)]))
    return result

def part1(data:str, verbose:bool=False) -> int:
    operations = parse(data)
    acc = 0
    for op in operations:
        op = op[::-1]
        print(op)
        if op[0] == "*":
            acc += multiply(*list(map(int, op[1:])))
        else:
            acc += add(*list(map(int, op[1:])))
    print(acc)