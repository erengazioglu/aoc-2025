"""
Advent of Code 2025 - Day 8 Part 2
"""

from util import read_input
from .part1 import get_all_distances, connect

def purge(pts, circuits):
    for circuit in circuits:
        for pt in circuit:
            if pt in pts:
                pts.remove(pt)


def part2(data:str, verbose:bool=False, use_sample=False) -> int:
    points = read_input(data, "tuples")
    dists = get_all_distances(points)
    dists.sort(key=lambda item: item[0] * -1)
    circuits = []
    iterations = 1000
    if use_sample:
        iterations = 10
    for i in range(iterations):
        shortest = dists.pop()
        connect(shortest[1], shortest[2], circuits)
    purge(points, circuits)
    if verbose:
        for pt in points:
            print(pt)
    connection = None
    while len(points):
        connection = dists.pop()
        connect(connection[1], connection[2], circuits)
        purge(points, circuits)
    return connection[1][0] * connection[2][0]