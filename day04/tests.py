from util import read_input
from .part1 import is_accessible

def initialize() -> tuple:
    map = read_input("inputs/04-sample")
    w = len(map[0])
    h = len(map)
    for line in map:
        print(line)
    return (map, w, h)


def test_neighbors(deps:tuple, cell, verbose=False):
    map, w, h = deps
    print(f"{cell} -> {"" if is_accessible(map, w, h, cell, True) else "not"} accessible")


def suite(verbose=False):
    deps = initialize()
    test_neighbors(deps, (2, 0))
    test_neighbors(deps, (0, 1))
    test_neighbors(deps, (1, 1))


if __name__ == "__main__":
    deps = initialize()
    suite(deps)