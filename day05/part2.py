"""
Advent of Code 2025 - Day 5 Part 2
"""

from .part1 import parse

def total(iset:list[tuple]) -> int:
    acc = 0
    print(iset)

    loop = True
    while loop:
        iset, loop = collapse(iset)
    for interval in iset:
        print(interval)
        acc += interval[1] - interval[0] + 1
    return acc


def collapse(iset:list[tuple]):
    for i, interval1 in enumerate(iset):
        print(f"{i}: {interval1}")
        for j, interval2 in enumerate(iset[i+1:]):
            print(f"  checking against {i + j + 1}, {interval2}")
            if does_intersect(interval1, interval2):
                print("    intersects!")
                iset[i] = union(interval1, interval2)
                iset.pop(i + j + 1)
                return (iset, True)
    return (iset, False)


def does_intersect(interval1:tuple, interval2:tuple) -> bool:
    interval3 = intersection(interval1, interval2)
    return interval3[0] <= interval3[1]


def intersection(interval1:tuple, interval2:tuple) -> tuple:
    return (max(interval1[0], interval2[0]), min(interval1[1], interval2[1]))


def union(interval1:tuple, interval2:tuple) -> tuple:
    return (min(interval1[0], interval2[0]), max(interval1[1], interval2[1]))


def add_interval(iset:list[tuple], interval:tuple) -> list[tuple]:
    for i, existing in enumerate(iset):
        if does_intersect(interval, existing):
            iset[i] = union(interval, existing)
            return iset
    iset.append(interval)
    return iset


def part2(data:str, verbose:bool=False) -> int:
    ranges, _ = parse(data)
    if verbose:
        print("Ranges:", ranges)
    
    fresh = []
    for interval in ranges:
        add_interval(fresh, interval)

    return total(fresh)