"""
Advent of Code 2025 - Day 8 Part 1
"""

from util import read_input, multiply
from math import sqrt

def distance(p1, p2):
    return sqrt(
        (p2[0] - p1[0]) ** 2
        + (p2[1] - p1[1]) ** 2
        + (p2[2] - p1[2]) ** 2
    )


def get_all_distances(pts) -> list[tuple]:
    result = []
    pts_len = len(pts)
    for i, pt in enumerate(pts):
        i += 1
        while i < pts_len:
            result.append((distance(pt, pts[i]), pt, pts[i]))
            i += 1
    return result


def purge(pts, circuits):
    for circuit in circuits:
        for pt in circuit:
            pts.remove(pt)


def connect(p1, p2, circuits):
    target = None
    for i, circuit in enumerate(circuits):
        if (p1 in circuit) or (p2 in circuit):
            if target:
                target |= circuit
                circuits.pop(i)
            else:
                circuit.add(p1)
                circuit.add(p2)
                target = circuit
    if not target:
        circuits.append(set((p1, p2)))

    return circuits


def part1(data:str, verbose:bool=False) -> int:
    input = read_input(data, "tuples")
    dists = get_all_distances(input)
    dists.sort(key=lambda item: item[0] * -1)
    # for dist in dists:
    #     print(f"{dist[0]:.2f}: ({dist[1]} | {dist[2]})")
    circuits = []
    for i in range(1000):
        shortest = dists.pop()
        connect(shortest[1], shortest[2], circuits)
    circuits.sort(key=lambda c: len(c), reverse=True)
    return multiply(len(circuits[0]), len(circuits[1]), len(circuits[2]))
    # purge(input, circuits)