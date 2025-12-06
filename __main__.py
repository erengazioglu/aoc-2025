import day01
import argparse

# def main():

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2025")
    parser.add_argument('-t', '--test', action='store_true', help='Run tests')
    parser.add_argument('-s', '--sample', action='store_true', help='Run tests')
    args = parser.parse_args()

    puzzle_input = "full"
    if args.sample:
        puzzle_input = "sample"
    if args.test:
        day01.tests.suite()
    else:
        print("Day 01 | Part 1:", day01.part1(f"inputs/01-{puzzle_input}"))
        print("Day 01 | Part 2:", day01.part2(f"inputs/01-{puzzle_input}"))

    # print(day01.part2())
